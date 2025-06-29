SAMPLE_LOG = """
+ : '>>>>> Start Test Output'
+ npx vitest --reporter=verbose run tests/mockComponents/EmbeddedStyles.vue tests/unit/src/cheerioManipulation.test.js tests/unit/src/formatMarkup.test.js

 RUN  v2.1.8 /testbed

 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Does no formatting
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Formats HTML to be diffable
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Applies custom formatting
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Logs warning if custom function does not return a string
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > diffableFormatter > No arguments
 × tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Retain just inner text
   → Snapshot `Format markup > HTML entity encoding > Retain just inner text 1` mismatched
 × tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Discard just inner text
   → Snapshot `Format markup > HTML entity encoding > Discard just inner text 1` mismatched
 × tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Retain just attributes
   → Snapshot `Format markup > HTML entity encoding > Retain just attributes 1` mismatched
 × tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Discard just attributes
   → Snapshot `Format markup > HTML entity encoding > Discard just attributes 1` mismatched
 × tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Retain both
   → Snapshot `Format markup > HTML entity encoding > Retain both 1` mismatched
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Discard both
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Comments > Formats comments accurately
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Comments > Removes comments
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Comments > Minifies empty comment
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Show empty attributes > Enabled
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Show empty attributes > Disabled
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Self Closing Tags > Enabled
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Self Closing Tags > Disabled
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Void elements > Formats void elements using HTML style
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Void elements > Formats void elements using XHTML style
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Void elements > Formats void elements using XML style
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Void elements > SVG elements > Formats SVG elements using HTML style
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Void elements > SVG elements > Formats SVG elements using XHTML style
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Void elements > SVG elements > Formats SVG elements using XML style
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Stubbed components > Fake TR in TBODY fragment
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Stubbed components > Fake TR in normal table
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Attributes Per Line > Attributes Per Line set to 0
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Attributes Per Line > Attributes Per Line set to Default
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Attributes Per Line > Attributes Per Line set to 2
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Attributes Per Line > Attributes Per Line set to 3
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Tags with whitespace preserved > Default whitespace preserved tags
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Tags with whitespace preserved > Provided tags are whitespace preserved tags
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Tags with whitespace preserved > No tags have whitespace preserved
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Tags with whitespace preserved > Returns occur after whitespace preserved tag
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Tags with whitespace preserved > Proper attribute indentation on nested child
 ✓ tests/unit/src/formatMarkup.test.js > Format markup > Tags with whitespace preserved > Proper attribute indentation on nested children
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Empty string
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Attributes to clear > Clears attributes
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Server rendered text > Removes server rendered attribute if setting enabled
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Server rendered text > Retains server rendered attribute if setting disabled
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > data-v-ids > Removes data-v-ids from real component
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > data-v-ids > Removes data-v-ids from string
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > data-v-ids > Keeps data-v-ids
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > data-v-ids > Remove empty attributes from data-v-id, but keep the v-id
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > InlineFunctions.vue > Functions kept
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > InlineFunctions.vue > Functions removed
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > InlineFunctions.vue > Props
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > SortAttributes.vue > Sorted
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > SortAttributes.vue > Unsorted
 × tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > EmbeddedStyles.vue > Embedded style tag
   → Snapshot `Cheerio Manipulation > EmbeddedStyles.vue > Embedded style tag 1` mismatched
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Add input values > Adds values into DOM
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Add input values > Does not add values into DOM
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Stringify attributes > Replaces attribute values including child components
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Stringify attributes > Replaces attribute values with stubbed child component
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Stringify attributes > Replaces prop values on children in shallow mounts
 ✓ tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > Stringify attributes > Does not stringify attributes

⎯⎯⎯⎯⎯⎯⎯ Failed Tests 6 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  tests/unit/src/cheerioManipulation.test.js > Cheerio Manipulation > EmbeddedStyles.vue > Embedded style tag
Error: Snapshot `Cheerio Manipulation > EmbeddedStyles.vue > Embedded style tag 1` mismatched

- Expected
+ Received

  <div>
-   <style>
-     .example {
-       border: 1px solid #F00;
-     }
-   </style>
  </div>

 ❯ tests/unit/src/cheerioManipulation.test.js:181:10
    179| 
    180|       expect(wrapper)
    181|         .toMatchInlineSnapshot(`
       |          ^
    182|           <div>
    183|             <style>

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/6]⎯

 FAIL  tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Retain just inner text
Error: Snapshot `Format markup > HTML entity encoding > Retain just inner text 1` mismatched

- Expected
+ Received

  <a href="http://site.com/?a=1&b=2">link</a>
- <pre><code>&lt;div title=&quot;text&quot;&gt;1 &amp; 2&nbsp;+&nbsp;3&lt;/div&gt;</code></pre>
+ <pre><code>&lt;div title="text"&gt;1 &amp; 2&nbsp;+&nbsp;3&lt;/div&gt;</code></pre>

 ❯ tests/unit/src/formatMarkup.test.js:130:10
    128| 
    129|       expect(input)
    130|         .toMatchInlineSnapshot(`
       |          ^
    131|           <a href="http://site.com/?a=1&b=2">link</a>
    132|           <pre><code>&lt;div title=&quot;text&quot;&gt;1 &amp; 2&nbsp;…

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[2/6]⎯

 FAIL  tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Discard just inner text
Error: Snapshot `Format markup > HTML entity encoding > Discard just inner text 1` mismatched

- Expected
+ Received

- <a href="http://site.com/?a=1&amp;b=2">link</a>
+ <a href="http://site.com/?a=1&b=2">link</a>
  <pre><code><div title="text">1 & 2 + 3</div></code></pre>

 ❯ tests/unit/src/formatMarkup.test.js:141:10
    139| 
    140|       expect(input)
    141|         .toMatchInlineSnapshot(`
       |          ^
    142|           <a href="http://site.com/?a=1&amp;b=2">link</a>
    143|           <pre><code><div title="text">1 & 2 + 3</div></code></pre>

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[3/6]⎯

 FAIL  tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Retain just attributes
Error: Snapshot `Format markup > HTML entity encoding > Retain just attributes 1` mismatched

- Expected
+ Received

- <a href="http://site.com/?a=1&amp;b=2">link</a>
+ <a href="http://site.com/?a=1&b=2">link</a>
  <pre><code><div title="text">1 & 2 + 3</div></code></pre>

 ❯ tests/unit/src/formatMarkup.test.js:152:10
    150| 
    151|       expect(input)
    152|         .toMatchInlineSnapshot(`
       |          ^
    153|           <a href="http://site.com/?a=1&amp;b=2">link</a>
    154|           <pre><code><div title="text">1 & 2 + 3</div></code></pre>

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[4/6]⎯

 FAIL  tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Discard just attributes
Error: Snapshot `Format markup > HTML entity encoding > Discard just attributes 1` mismatched

- Expected
+ Received

  <a href="http://site.com/?a=1&b=2">link</a>
- <pre><code>&lt;div title=&quot;text&quot;&gt;1 &amp; 2&nbsp;+&nbsp;3&lt;/div&gt;</code></pre>
+ <pre><code>&lt;div title="text"&gt;1 &amp; 2&nbsp;+&nbsp;3&lt;/div&gt;</code></pre>

 ❯ tests/unit/src/formatMarkup.test.js:163:10
    161| 
    162|       expect(input)
    163|         .toMatchInlineSnapshot(`
       |          ^
    164|           <a href="http://site.com/?a=1&b=2">link</a>
    165|           <pre><code>&lt;div title=&quot;text&quot;&gt;1 &amp; 2&nbsp;…

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[5/6]⎯

 FAIL  tests/unit/src/formatMarkup.test.js > Format markup > HTML entity encoding > Retain both
Error: Snapshot `Format markup > HTML entity encoding > Retain both 1` mismatched

- Expected
+ Received

- <a href="http://site.com/?a=1&amp;b=2">link</a>
+ <a href="http://site.com/?a=1&b=2">link</a>
- <pre><code>&lt;div title=&quot;text&quot;&gt;1 &amp; 2&nbsp;+&nbsp;3&lt;/div&gt;</code></pre>
+ <pre><code>&lt;div title="text"&gt;1 &amp; 2&nbsp;+&nbsp;3&lt;/div&gt;</code></pre>

 ❯ tests/unit/src/formatMarkup.test.js:174:10
    172| 
    173|       expect(input)
    174|         .toMatchInlineSnapshot(`
       |          ^
    175|           <a href="http://site.com/?a=1&amp;b=2">link</a>
    176|           <pre><code>&lt;div title=&quot;text&quot;&gt;1 &amp; 2&nbsp;…

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[6/6]⎯

  Snapshots  6 failed
 Test Files  2 failed (2)
      Tests  6 failed | 50 passed (56)
   Start at  15:38:52
   Duration  1.74s (transform 329ms, setup 20ms, collect 471ms, tests 526ms, environment 759ms, prepare 880ms)

+ : '>>>>> End Test Output'
"""
