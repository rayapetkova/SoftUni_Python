const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

const host = 'http://localhost:3000'; // Application host (NOT service host - that can be anything)

const DEBUG = false;
const slowMo = 500;

const mockData = {
  list: [
    {
      product: "Milk",
      count: 2,
      price: 3,
      _id: '1001',
    },
    {
      product: "Apple",
      count: 5,
      price: 2,
      _id: '1002',
    },
  ],
};

const endpoints = {
  catalog: '/jsonstore/grocery',
  byId: (id) => `/jsonstore/grocery/${id}`,
};

let browser;
let context;
let page;

describe('E2E tests', function () {
  // Setup
  this.timeout(DEBUG ? 120000 : 7000);
  before(
    async () =>
    (browser = await chromium.launch(
      DEBUG ? { headless: false, slowMo } : {}
    ))
  );
  after(async () => await browser.close());
  beforeEach(async () => {
    context = await browser.newContext();
    setupContext(context);
    page = await context.newPage();
  });
  afterEach(async () => {
    await page.close();
    await context.close();
  });

  // Test proper
  describe('Grocery List', () => {
    it('Load Product', async () => {
      const data = mockData.list;
      const { get } = await handle(endpoints.catalog);
      get(data);

      await page.goto(host);
      await page.waitForSelector('#load-product');

      await page.click('#load-product');

      const allProducts = await page.$$eval(`tbody tr`, (t) =>
        t.map((s) => s.textContent)
      );

      expect(allProducts[0]).to.equal(`${data[0].product}23UpdateDelete`);
      expect(allProducts[0]).to.equal(`Milk${data[0].count}3UpdateDelete`);
      expect(allProducts[0]).to.equal(`Milk2${data[0].price}UpdateDelete`);

      expect(allProducts[1]).to.equal(`${data[1].product}52UpdateDelete`);
      expect(allProducts[1]).to.equal(`Apple${data[1].count}2UpdateDelete`);
      expect(allProducts[1]).to.equal(`Apple5${data[1].price}UpdateDelete`);
    });

    it('Add Product', async () => {
      await page.goto(host);

      const { post } = await handle(endpoints.catalog);
      const { onRequest } = post();

      await page.waitForSelector('.list');

      await page.fill('#product', 'Bread');
      await page.fill('#count', '3');
      await page.fill('#price', '1');

      const [request] = await Promise.all([
        onRequest(),
        page.click('#add-product'),
      ]);

      const postData = JSON.parse(request.postData());

      expect(postData.product).to.equal('Bread');
      expect(postData.count).to.equal('3');
      expect(postData.price).to.equal('1');
    });

    it('Remove Product', async () => {
      const data = mockData.list[0];
      await page.goto(host);
      const { del } = await handle(endpoints.byId(data._id));
      const { onResponse, isHandled } = del({ id: data._id });

      await page.click('#load-product');

      await page.waitForSelector('#tbody>tr');

      await Promise.all([
        onResponse(),
        page.click(
          `#tbody tr button:nth-child(2)`
        ),
      ]);

      expect(isHandled()).to.be.true;
    });


    it('Edit Task (Has Input & Submit Button)', async () => {
      await page.goto(host);

      await page.click('#load-product');
      await page.waitForSelector('#tbody>tr');
      await page.click('#tbody tr button:nth-child(1)');
      const allProduct = await page.$$eval(`.list input`, (t) =>
        t.map((s) => s.value)
      );

      expect(allProduct[0]).to.include('Milk');
      expect(allProduct[1]).to.include('2');
      expect(allProduct[2]).to.include('3');
    });

    it('Edit Protuct (Makes API Call)', async () => {
      const data = mockData.list[0];
      await page.goto(host);
      const { patch } = await handle(endpoints.byId(data._id));
      const { onRequest } = patch({ id: data._id });

      await page.click('#load-product');
      await page.waitForSelector('#tbody>tr');
      await page.click('#tbody tr button:nth-child(1)');
      await page.fill('#product', data.product + '2');

      const [request] = await Promise.all([
        onRequest(),
        page.click('#update-product'),
      ]);

      const postData = JSON.parse(request.postData());
      expect(postData.product).to.equal(data.product + '2');
    });
  });
});

async function setupContext(context) {
  // Catalog and Details
  await handleContext(context, endpoints.catalog, { get: mockData.list });
  await handleContext(context, endpoints.catalog, { post: mockData.list[0] });

  await handleContext(context, endpoints.byId('1001'), {
    get: mockData.list[0],
  });

  // Block external calls
  await context.route(
    (url) => url.href.slice(0, host.length) != host,
    (route) => {
      if (DEBUG) {
        console.log('Preventing external call to ' + route.request().url());
      }
      route.abort();
    }
  );
}

function handle(match, handlers) {
  return handleRaw.call(page, match, handlers);
}

function handleContext(context, match, handlers) {
  return handleRaw.call(context, match, handlers);
}

async function handleRaw(match, handlers) {
  const methodHandlers = {};
  const result = {
    get: (returns, options) => request('GET', returns, options),
    get2: (returns, options) => request('GET', returns, options),
    post: (returns, options) => request('POST', returns, options),
    put: (returns, options) => request('PUT', returns, options),
    patch: (returns, options) => request('PATCH', returns, options),
    del: (returns, options) => request('DELETE', returns, options),
    delete: (returns, options) => request('DELETE', returns, options),
  };

  const context = this;

  await context.route(urlPredicate, (route, request) => {
    if (DEBUG) {
      console.log('>>>', request.method(), request.url());
    }

    const handler = methodHandlers[request.method().toLowerCase()];
    if (handler == undefined) {
      route.continue();
    } else {
      handler(route, request);
    }
  });

  if (handlers) {
    for (let method in handlers) {
      if (typeof handlers[method] == 'function') {
        handlers[method](result[method]);
      } else {
        result[method](handlers[method]);
      }
    }
  }

  return result;

  function request(method, returns, options) {
    let handled = false;

    methodHandlers[method.toLowerCase()] = (route, request) => {
      handled = true;
      route.fulfill(respond(returns, options));
    };

    return {
      onRequest: () => context.waitForRequest(urlPredicate),
      onResponse: () => context.waitForResponse(urlPredicate),
      isHandled: () => handled,
    };
  }

  function urlPredicate(current) {
    if (current instanceof URL) {
      return current.href.toLowerCase().includes(match.toLowerCase());
    } else {
      return current.url().toLowerCase().includes(match.toLowerCase());
    }
  }
}

function respond(data, options = {}) {
  options = Object.assign(
    {
      json: true,
      status: 200,
    },
    options
  );

  const headers = {
    'Access-Control-Allow-Origin': '*',
  };
  if (options.json) {
    headers['Content-Type'] = 'application/json';
    data = JSON.stringify(data);
  }

  return {
    status: options.status,
    headers,
    body: data,
  };
}
