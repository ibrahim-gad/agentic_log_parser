task_adobe__spectrum_web_components_5118 = """
+ : '>>>>> Start Test Output'
+ npm run test:base tests/lib/rules/restricted-component-names.js

> eslint-plugin-vue@9.31.0 test:base
> mocha "tests/lib/**/*.js" --reporter dot tests/lib/rules/restricted-component-names.js


 Exception during run: Error: Cannot find module '../../../lib/rules/restricted-component-names'
Require stack:
- /testbed/tests/lib/rules/restricted-component-names.js
    at Module._resolveFilename (node:internal/modules/cjs/loader:1212:15)
    at Module._load (node:internal/modules/cjs/loader:1043:27)
    at Module.require (node:internal/modules/cjs/loader:1298:19)
    at require (node:internal/modules/helpers:182:18)
    at Object.<anonymous> (/testbed/tests/lib/rules/restricted-component-names.js:8:14)
    at Module._compile (node:internal/modules/cjs/loader:1529:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1613:10)
    at Module.load (node:internal/modules/cjs/loader:1275:32)
    at Module._load (node:internal/modules/cjs/loader:1096:12)
    at cjsLoader (node:internal/modules/esm/translators:298:15)
    at ModuleWrap.<anonymous> (node:internal/modules/esm/translators:240:7)
    at ModuleJob.run (node:internal/modules/esm/module_job:263:25)
    at async ModuleLoader.import (node:internal/modules/esm/loader:540:24)
    at async formattedImport (/testbed/node_modules/mocha/lib/nodejs/esm-utils.js:9:14)
    at async exports.requireOrImport (/testbed/node_modules/mocha/lib/nodejs/esm-utils.js:42:28)
    at async exports.loadFilesAsync (/testbed/node_modules/mocha/lib/nodejs/esm-utils.js:100:20)
    at async singleRun (/testbed/node_modules/mocha/lib/cli/run-helpers.js:162:3)
    at async exports.handler (/testbed/node_modules/mocha/lib/cli/run.js:375:5) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [ '/testbed/tests/lib/rules/restricted-component-names.js' ]
}
+ : '>>>>> End Test Output'
"""
