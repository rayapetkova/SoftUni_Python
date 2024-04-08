const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

const host = 'http://localhost:3000'; // Application host (NOT service host - that can be anything)

const DEBUG = false;
const slowMo = 500;

const mockData = {
  list: [
    {
      name: 'Go Shopping',
      _id: '1001',
    },
    {
      name: 'Go Karting',
      _id: '1002',
    },
  ],
};

const endpoints = {
  catalog: '/jsonstore/tasks',
  byId: (id) => `/jsonstore/tasks/${id}`,
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
  describe('Todo List Tests', () => {
    it('Load Tasks', async () => {
      const data = mockData.list;
      const { get } = await handle(endpoints.catalog);
      get(data);

      await page.goto(host);
      await page.waitForSelector('#load-button');

      await page.click('#load-button');

      const allTasks = await page.$$eval(`#todo-list li`, (t) =>
        t.map((s) => s.textContent)
      );

      expect(allTasks[0]).to.equal(`${data[0].name}RemoveEdit`);
      expect(allTasks[1]).to.equal(`${data[1].name}RemoveEdit`);
    });

    it('Add Task', async () => {
      const data = mockData.list[0];
      await page.goto(host);

      const { post } = await handle(endpoints.catalog);
      const { onRequest } = post();

      await page.waitForSelector('#title');

      await page.fill('#title', data.name + '1');

      const [request] = await Promise.all([
        onRequest(),
        page.click('#add-button'),
      ]);

      const postData = JSON.parse(request.postData());

      expect(postData.name).to.equal(data.name + '1');
    });

    it('Remove Task', async () => {
      const data = mockData.list[0];
      await page.goto(host);
      const { del } = await handle(endpoints.byId(data._id));
      const { onResponse, isHandled } = del({ id: data._id });

      await page.click('#load-button');

      await page.waitForSelector('#todo-list>li');

      await Promise.all([
        onResponse(),
        page.click(
          `#todo-list li button:nth-child(2)`
        ),
      ]);

      expect(isHandled()).to.be.true;
    });

    
    it('Edit Task (Has Input & Submit Button)', async () => {
      await page.goto(host);

      await page.click('#load-button');
      await page.waitForSelector('#todo-list>li');
      await page.click('#todo-list li button:nth-child(3)');
      const allTasks = await page.$$eval(`#todo-list li`, (t) =>
        t.map((s) => s.innerHTML)
      );

      expect(allTasks[0]).to.include('input');
      expect(allTasks[0]).to.include('Submit');
    });

    it('Edit Task (Makes API Call)', async () => {
      const data = mockData.list[0];
      await page.goto(host);
      const { patch } = await handle(endpoints.byId(data._id));
      const { onRequest } = patch({ id: data._id });

      await page.click('#load-button');
      await page.waitForSelector('#todo-list>li');
      await page.click('#todo-list li button:nth-child(3)');
      await page.fill('#todo-list li input', data.name + ' In Mall');
      const [request] = await Promise.all([
        onRequest(),
        page.click('#todo-list li button:nth-child(3)'),
      ]);

      const postData = JSON.parse(request.postData());

      expect(postData.name).to.equal(data.name + ' In Mall');
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
