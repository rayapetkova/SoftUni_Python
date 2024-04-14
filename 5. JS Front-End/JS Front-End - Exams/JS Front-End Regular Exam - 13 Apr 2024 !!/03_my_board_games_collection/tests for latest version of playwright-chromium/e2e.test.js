const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

const host = 'http://localhost:3000'; // Application host (NOT service host - that can be anything)

const DEBUG = false;
const slowMo = 500;

const mockData = {
  list: [
    {
      name: 'Bug 1',
      type: '100',
      players: '100',
      _id: '1001',
    },
    { name: 'Bug 2',
      type: '1',
      players: '200',
      _id: '1002',
    },
    {
      name: 'Bug 3',
      type: '1',
      players: '300',
      _id: '1003',
    },
    {
      name: 'Bug 4',
      type: '1',
      players: '400',
      _id: '1004',
    },
  ],
};

const endpoints = {
  catalog: '/jsonstore/games',
  byId: (id) => `/jsonstore/games/${id}`,
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

  describe('Board Games Collection', () => {
    it('Load Games', async () => {
      const data = mockData.list;
      const { get } = await handle(endpoints.catalog);
      get(data);

      await page.goto(host);
      await page.waitForSelector('#load-games');

      await page.click('#load-games');

      const list = await page.$$eval(`#games #games-list .board-game`, (t) =>
        t.map((s) => s.textContent)
      );
      expect(list.length).to.equal(data.length);

    });

   it('Add Game', async () => {
      const data = mockData.list[0];
      await page.goto(host);

      const { post } = await handle(endpoints.catalog);
      const { onRequest } = post();

      await page.waitForSelector('#form');
      await page.fill('#g-name', data.name);
      await page.fill('#type', data.type);
      await page.fill('#players', data.players);

      const [request] = await Promise.all([
        onRequest(),
        page.click('#add-game'),
      ]);

      const postData = JSON.parse(request.postData());
      
      expect(postData.name).to.equal(data.name);
      expect(postData.type).to.equal(data.type);
      expect(postData.players).to.equal(data.players);

      const [name] = await page.$$eval(`#g-name`, (t) =>
        t.map((s) => s.value)
      );
      const [typeGame] = await page.$$eval(`#type`, (t) =>
        t.map((s) => s.value)
      );

      const [maxPlayers] = await page.$$eval(`#players`, (t) =>
        t.map((s) => s.value)
      );

      expect(name).to.equal('');
      expect(typeGame).to.equal('');
      expect(maxPlayers).to.equal('');
    });

    it('Edit Game (Has Input)', async () => {
      await page.goto(host);
      const data = mockData.list[0];

      await page.click('#load-games');
      await page.waitForSelector('#games-list');
      await page.click('#games-list .board-game .change-btn');

      const allCourse = await page.$$eval(`#form input`, (t) =>
        t.map((s) => s.value)
      );

   

      expect(allCourse[0]).to.include(data.name);
      expect(allCourse[1]).to.include(data.type);
      expect(allCourse[2]).to.include(data.players);

    });

    it('Edit Game (Makes API Call)', async () => {
      const data = mockData.list[0];
      await page.goto(host);
      const { patch } = await handle(endpoints.byId(data._id));
      const { onRequest } = patch({ id: data._id });

      await page.click('#load-games');
      await page.waitForSelector('#games-list');
      await page.click('#games-list .board-game .change-btn');
      await page.fill('#g-name', data.name + '2');

      const [request] = await Promise.all([
        onRequest(),
        page.click('#edit-game'),
      ]);

      const postData = JSON.parse(request.postData());
      expect(postData.name).to.equal(data.name + '2');
    });

    it('Delete Game', async () => {
      const data = mockData.list[0];
      await page.goto(host);
      const { del } = await handle(endpoints.byId(data._id));
      const { onResponse, isHandled } = del({ id: data._id });

      await page.click('#load-games');

      await page.waitForSelector('#games-list');

      await Promise.all([
        onResponse(),
        page.click(
          `#games-list .board-game .delete-btn`
        ),
      ]);

      expect(isHandled()).to.be.true;
    });
  });
});

async function setupContext(context) {
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

 await handleContext(context, endpoints.byId('1001'), {
   get: mockData.list[0],
 });

 await handleContext(context, endpoints.catalog, { post: mockData.list[0] });
 // Catalog and Details
 await handleContext(context, endpoints.catalog, { get: mockData.list });
 

 

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
  }); ``

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
