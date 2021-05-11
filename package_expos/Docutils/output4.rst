<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="generator" content="Docutils 0.16: http://docutils.sourceforge.net/" />
<title>output3.rst</title>
<style type="text/css">

/*
:Author: David Goodger (goodger@python.org)
:Id: $Id: html4css1.css 7952 2016-07-26 18:15:59Z milde $
:Copyright: This stylesheet has been placed in the public domain.

Default cascading style sheet for the HTML output of Docutils.

See http://docutils.sf.net/docs/howto/html-stylesheets.html for how to
customize this style sheet.
*/

/* used to remove borders from tables and images */
.borderless, table.borderless td, table.borderless th {
  border: 0 }

table.borderless td, table.borderless th {
  /* Override padding for "table.docutils td" with "! important".
     The right padding separates the table cells. */
  padding: 0 0.5em 0 0 ! important }

.first {
  /* Override more specific margin styles with "! important". */
  margin-top: 0 ! important }

.last, .with-subtitle {
  margin-bottom: 0 ! important }

.hidden {
  display: none }

.subscript {
  vertical-align: sub;
  font-size: smaller }

.superscript {
  vertical-align: super;
  font-size: smaller }

a.toc-backref {
  text-decoration: none ;
  color: black }

blockquote.epigraph {
  margin: 2em 5em ; }

dl.docutils dd {
  margin-bottom: 0.5em }

object[type="image/svg+xml"], object[type="application/x-shockwave-flash"] {
  overflow: hidden;
}

/* Uncomment (and remove this text!) to get bold-faced definition list terms
dl.docutils dt {
  font-weight: bold }
*/

div.abstract {
  margin: 2em 5em }

div.abstract p.topic-title {
  font-weight: bold ;
  text-align: center }

div.admonition, div.attention, div.caution, div.danger, div.error,
div.hint, div.important, div.note, div.tip, div.warning {
  margin: 2em ;
  border: medium outset ;
  padding: 1em }

div.admonition p.admonition-title, div.hint p.admonition-title,
div.important p.admonition-title, div.note p.admonition-title,
div.tip p.admonition-title {
  font-weight: bold ;
  font-family: sans-serif }

div.attention p.admonition-title, div.caution p.admonition-title,
div.danger p.admonition-title, div.error p.admonition-title,
div.warning p.admonition-title, .code .error {
  color: red ;
  font-weight: bold ;
  font-family: sans-serif }

/* Uncomment (and remove this text!) to get reduced vertical space in
   compound paragraphs.
div.compound .compound-first, div.compound .compound-middle {
  margin-bottom: 0.5em }

div.compound .compound-last, div.compound .compound-middle {
  margin-top: 0.5em }
*/

div.dedication {
  margin: 2em 5em ;
  text-align: center ;
  font-style: italic }

div.dedication p.topic-title {
  font-weight: bold ;
  font-style: normal }

div.figure {
  margin-left: 2em ;
  margin-right: 2em }

div.footer, div.header {
  clear: both;
  font-size: smaller }

div.line-block {
  display: block ;
  margin-top: 1em ;
  margin-bottom: 1em }

div.line-block div.line-block {
  margin-top: 0 ;
  margin-bottom: 0 ;
  margin-left: 1.5em }

div.sidebar {
  margin: 0 0 0.5em 1em ;
  border: medium outset ;
  padding: 1em ;
  background-color: #ffffee ;
  width: 40% ;
  float: right ;
  clear: right }

div.sidebar p.rubric {
  font-family: sans-serif ;
  font-size: medium }

div.system-messages {
  margin: 5em }

div.system-messages h1 {
  color: red }

div.system-message {
  border: medium outset ;
  padding: 1em }

div.system-message p.system-message-title {
  color: red ;
  font-weight: bold }

div.topic {
  margin: 2em }

h1.section-subtitle, h2.section-subtitle, h3.section-subtitle,
h4.section-subtitle, h5.section-subtitle, h6.section-subtitle {
  margin-top: 0.4em }

h1.title {
  text-align: center }

h2.subtitle {
  text-align: center }

hr.docutils {
  width: 75% }

img.align-left, .figure.align-left, object.align-left, table.align-left {
  clear: left ;
  float: left ;
  margin-right: 1em }

img.align-right, .figure.align-right, object.align-right, table.align-right {
  clear: right ;
  float: right ;
  margin-left: 1em }

img.align-center, .figure.align-center, object.align-center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

table.align-center {
  margin-left: auto;
  margin-right: auto;
}

.align-left {
  text-align: left }

.align-center {
  clear: both ;
  text-align: center }

.align-right {
  text-align: right }

/* reset inner alignment in figures */
div.align-right {
  text-align: inherit }

/* div.align-center * { */
/*   text-align: left } */

.align-top    {
  vertical-align: top }

.align-middle {
  vertical-align: middle }

.align-bottom {
  vertical-align: bottom }

ol.simple, ul.simple {
  margin-bottom: 1em }

ol.arabic {
  list-style: decimal }

ol.loweralpha {
  list-style: lower-alpha }

ol.upperalpha {
  list-style: upper-alpha }

ol.lowerroman {
  list-style: lower-roman }

ol.upperroman {
  list-style: upper-roman }

p.attribution {
  text-align: right ;
  margin-left: 50% }

p.caption {
  font-style: italic }

p.credits {
  font-style: italic ;
  font-size: smaller }

p.label {
  white-space: nowrap }

p.rubric {
  font-weight: bold ;
  font-size: larger ;
  color: maroon ;
  text-align: center }

p.sidebar-title {
  font-family: sans-serif ;
  font-weight: bold ;
  font-size: larger }

p.sidebar-subtitle {
  font-family: sans-serif ;
  font-weight: bold }

p.topic-title {
  font-weight: bold }

pre.address {
  margin-bottom: 0 ;
  margin-top: 0 ;
  font: inherit }

pre.literal-block, pre.doctest-block, pre.math, pre.code {
  margin-left: 2em ;
  margin-right: 2em }

pre.code .ln { color: grey; } /* line numbers */
pre.code, code { background-color: #eeeeee }
pre.code .comment, code .comment { color: #5C6576 }
pre.code .keyword, code .keyword { color: #3B0D06; font-weight: bold }
pre.code .literal.string, code .literal.string { color: #0C5404 }
pre.code .name.builtin, code .name.builtin { color: #352B84 }
pre.code .deleted, code .deleted { background-color: #DEB0A1}
pre.code .inserted, code .inserted { background-color: #A3D289}

span.classifier {
  font-family: sans-serif ;
  font-style: oblique }

span.classifier-delimiter {
  font-family: sans-serif ;
  font-weight: bold }

span.interpreted {
  font-family: sans-serif }

span.option {
  white-space: nowrap }

span.pre {
  white-space: pre }

span.problematic {
  color: red }

span.section-subtitle {
  /* font-size relative to parent (h1..h6 element) */
  font-size: 80% }

table.citation {
  border-left: solid 1px gray;
  margin-left: 1px }

table.docinfo {
  margin: 2em 4em }

table.docutils {
  margin-top: 0.5em ;
  margin-bottom: 0.5em }

table.footnote {
  border-left: solid 1px black;
  margin-left: 1px }

table.docutils td, table.docutils th,
table.docinfo td, table.docinfo th {
  padding-left: 0.5em ;
  padding-right: 0.5em ;
  vertical-align: top }

table.docutils th.field-name, table.docinfo th.docinfo-name {
  font-weight: bold ;
  text-align: left ;
  white-space: nowrap ;
  padding-left: 0 }

/* "booktabs" style (no vertical lines) */
table.docutils.booktabs {
  border: 0px;
  border-top: 2px solid;
  border-bottom: 2px solid;
  border-collapse: collapse;
}
table.docutils.booktabs * {
  border: 0px;
}
table.docutils.booktabs th {
  border-bottom: thin solid;
  text-align: left;
}

h1 tt.docutils, h2 tt.docutils, h3 tt.docutils,
h4 tt.docutils, h5 tt.docutils, h6 tt.docutils {
  font-size: 100% }

ul.auto-toc {
  list-style-type: none }

</style>
</head>
<body>
<div class="document">


<p>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; ?&gt;
&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.0 Transitional//EN&quot; &quot;<a class="reference external" href="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd</a>&quot;&gt;
&lt;html xmlns=&quot;<a class="reference external" href="http://www.w3.org/1999/xhtml">http://www.w3.org/1999/xhtml</a>&quot; xml:lang=&quot;en&quot; lang=&quot;en&quot;&gt;
&lt;head&gt;
&lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=utf-8&quot; /&gt;
&lt;meta name=&quot;generator&quot; content=&quot;Docutils 0.16: http://docutils.sourceforge.net/&quot; /&gt;
&lt;title&gt;index.htm&lt;/title&gt;
&lt;style type=&quot;text/css&quot;&gt;</p>
<p>/*
:Author: David Goodger (<a class="reference external" href="mailto:goodger&#64;python.org">goodger&#64;python.org</a>)
:Id: $Id: html4css1.css 7952 2016-07-26 18:15:59Z milde $
:Copyright: This stylesheet has been placed in the public domain.</p>
<p>Default cascading style sheet for the HTML output of Docutils.</p>
<p>See <a class="reference external" href="http://docutils.sf.net/docs/howto/html-stylesheets.html">http://docutils.sf.net/docs/howto/html-stylesheets.html</a> for how to
customize this style sheet.
<a href="#id1"><span class="problematic" id="id2">*</span></a>/</p>
<div class="system-message" id="id1">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 17); <em><a href="#id2">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<p>/* used to remove borders from tables and images <a href="#id3"><span class="problematic" id="id4">*</span></a>/
.borderless, table.borderless td, table.borderless th {</p>
<div class="system-message" id="id3">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 21); <em><a href="#id4">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 23)</p>
Unexpected indentation.</div>
<blockquote>
border: 0 }</blockquote>
<dl class="docutils">
<dt>table.borderless td, table.borderless th {</dt>
<dd><dl class="first docutils">
<dt>/* Override padding for &quot;table.docutils td&quot; with &quot;! important&quot;.</dt>
<dd><p class="first">The right padding separates the table cells. <a href="#id5"><span class="problematic" id="id6">*</span></a>/</p>
<div class="last system-message" id="id5">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 27); <em><a href="#id6">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
</dd>
</dl>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 28)</p>
Definition list ends without a blank line; unexpected unindent.</div>
<p class="last">padding: 0 0.5em 0 0 ! important }</p>
</dd>
<dt>.first {</dt>
<dd><p class="first">/* Override more specific margin styles with &quot;! important&quot;. <a href="#id7"><span class="problematic" id="id8">*</span></a>/
margin-top: 0 ! important }</p>
<div class="last system-message" id="id7">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 31); <em><a href="#id8">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
</dd>
<dt>.last, .with-subtitle {</dt>
<dd>margin-bottom: 0 ! important }</dd>
<dt>.hidden {</dt>
<dd>display: none }</dd>
<dt>.subscript {</dt>
<dd>vertical-align: sub;
font-size: smaller }</dd>
<dt>.superscript {</dt>
<dd>vertical-align: super;
font-size: smaller }</dd>
<dt>a.toc-backref {</dt>
<dd>text-decoration: none ;
color: black }</dd>
<dt>blockquote.epigraph {</dt>
<dd>margin: 2em 5em ; }</dd>
<dt>dl.docutils dd {</dt>
<dd>margin-bottom: 0.5em }</dd>
<dt>object[type=&quot;image/svg+xml&quot;], object[type=&quot;application/x-shockwave-flash&quot;] {</dt>
<dd>overflow: hidden;</dd>
</dl>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 60)</p>
Definition list ends without a blank line; unexpected unindent.</div>
<p>}</p>
<p>/* Uncomment (and remove this text!) to get bold-faced definition list terms
dl.docutils dt {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 64)</p>
Unexpected indentation.</div>
<blockquote>
font-weight: bold }</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 65)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p><a href="#id9"><span class="problematic" id="id10">*</span></a>/</p>
<div class="system-message" id="id9">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 65); <em><a href="#id10">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<dl class="docutils">
<dt>div.abstract {</dt>
<dd>margin: 2em 5em }</dd>
<dt>div.abstract p.topic-title {</dt>
<dd>font-weight: bold ;
text-align: center }</dd>
</dl>
<p>div.admonition, div.attention, div.caution, div.danger, div.error,
div.hint, div.important, div.note, div.tip, div.warning {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 76)</p>
Unexpected indentation.</div>
<blockquote>
margin: 2em ;
border: medium outset ;
padding: 1em }</blockquote>
<p>div.admonition p.admonition-title, div.hint p.admonition-title,
div.important p.admonition-title, div.note p.admonition-title,
div.tip p.admonition-title {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 83)</p>
Unexpected indentation.</div>
<blockquote>
font-weight: bold ;
font-family: sans-serif }</blockquote>
<p>div.attention p.admonition-title, div.caution p.admonition-title,
div.danger p.admonition-title, div.error p.admonition-title,
div.warning p.admonition-title, .code .error {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 89)</p>
Unexpected indentation.</div>
<blockquote>
color: red ;
font-weight: bold ;
font-family: sans-serif }</blockquote>
<dl class="docutils">
<dt>/* Uncomment (and remove this text!) to get reduced vertical space in</dt>
<dd>compound paragraphs.</dd>
<dt>div.compound .compound-first, div.compound .compound-middle {</dt>
<dd>margin-bottom: 0.5em }</dd>
<dt>div.compound .compound-last, div.compound .compound-middle {</dt>
<dd>margin-top: 0.5em }</dd>
</dl>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 100)</p>
Definition list ends without a blank line; unexpected unindent.</div>
<p><a href="#id11"><span class="problematic" id="id12">*</span></a>/</p>
<div class="system-message" id="id11">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 100); <em><a href="#id12">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<dl class="docutils">
<dt>div.dedication {</dt>
<dd>margin: 2em 5em ;
text-align: center ;
font-style: italic }</dd>
<dt>div.dedication p.topic-title {</dt>
<dd>font-weight: bold ;
font-style: normal }</dd>
<dt>div.figure {</dt>
<dd>margin-left: 2em ;
margin-right: 2em }</dd>
<dt>div.footer, div.header {</dt>
<dd>clear: both;
font-size: smaller }</dd>
<dt>div.line-block {</dt>
<dd>display: block ;
margin-top: 1em ;
margin-bottom: 1em }</dd>
<dt>div.line-block div.line-block {</dt>
<dd>margin-top: 0 ;
margin-bottom: 0 ;
margin-left: 1.5em }</dd>
<dt>div.sidebar {</dt>
<dd>margin: 0 0 0.5em 1em ;
border: medium outset ;
padding: 1em ;
background-color: #ffffee ;
width: 40% ;
float: right ;
clear: right }</dd>
<dt>div.sidebar p.rubric {</dt>
<dd>font-family: sans-serif ;
font-size: medium }</dd>
<dt>div.system-messages {</dt>
<dd>margin: 5em }</dd>
<dt>div.system-messages h1 {</dt>
<dd>color: red }</dd>
<dt>div.system-message {</dt>
<dd>border: medium outset ;
padding: 1em }</dd>
<dt>div.system-message p.system-message-title {</dt>
<dd>color: red ;
font-weight: bold }</dd>
<dt>div.topic {</dt>
<dd>margin: 2em }</dd>
</dl>
<p>h1.section-subtitle, h2.section-subtitle, h3.section-subtitle,
h4.section-subtitle, h5.section-subtitle, h6.section-subtitle {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 161)</p>
Unexpected indentation.</div>
<blockquote>
margin-top: 0.4em }</blockquote>
<dl class="docutils">
<dt>h1.title {</dt>
<dd>text-align: center }</dd>
<dt>h2.subtitle {</dt>
<dd>text-align: center }</dd>
<dt>hr.docutils {</dt>
<dd>width: 75% }</dd>
<dt>img.align-left, .figure.align-left, object.align-left, table.align-left {</dt>
<dd>clear: left ;
float: left ;
margin-right: 1em }</dd>
<dt>img.align-right, .figure.align-right, object.align-right, table.align-right {</dt>
<dd>clear: right ;
float: right ;
margin-left: 1em }</dd>
<dt>img.align-center, .figure.align-center, object.align-center {</dt>
<dd>display: block;
margin-left: auto;
margin-right: auto;</dd>
</dl>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 186)</p>
Definition list ends without a blank line; unexpected unindent.</div>
<p>}</p>
<dl class="docutils">
<dt>table.align-center {</dt>
<dd>margin-left: auto;
margin-right: auto;</dd>
</dl>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 191)</p>
Definition list ends without a blank line; unexpected unindent.</div>
<p>}</p>
<dl class="docutils">
<dt>.align-left {</dt>
<dd>text-align: left }</dd>
<dt>.align-center {</dt>
<dd>clear: both ;
text-align: center }</dd>
<dt>.align-right {</dt>
<dd>text-align: right }</dd>
</dl>
<p>/* reset inner alignment in figures <a href="#id13"><span class="problematic" id="id14">*</span></a>/
div.align-right {</p>
<div class="system-message" id="id13">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 203); <em><a href="#id14">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 205)</p>
Unexpected indentation.</div>
<blockquote>
text-align: inherit }</blockquote>
<p>/* div.align-center * { <em>/
/</em>   text-align: left } <a href="#id15"><span class="problematic" id="id16">*</span></a>/</p>
<div class="system-message" id="id15">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 207); <em><a href="#id16">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<dl class="docutils">
<dt>.align-top    {</dt>
<dd>vertical-align: top }</dd>
<dt>.align-middle {</dt>
<dd>vertical-align: middle }</dd>
<dt>.align-bottom {</dt>
<dd>vertical-align: bottom }</dd>
<dt>ol.simple, ul.simple {</dt>
<dd>margin-bottom: 1em }</dd>
<dt>ol.arabic {</dt>
<dd>list-style: decimal }</dd>
<dt>ol.loweralpha {</dt>
<dd>list-style: lower-alpha }</dd>
<dt>ol.upperalpha {</dt>
<dd>list-style: upper-alpha }</dd>
<dt>ol.lowerroman {</dt>
<dd>list-style: lower-roman }</dd>
<dt>ol.upperroman {</dt>
<dd>list-style: upper-roman }</dd>
<dt>p.attribution {</dt>
<dd>text-align: right ;
margin-left: 50% }</dd>
<dt>p.caption {</dt>
<dd>font-style: italic }</dd>
<dt>p.credits {</dt>
<dd>font-style: italic ;
font-size: smaller }</dd>
<dt>p.label {</dt>
<dd>white-space: nowrap }</dd>
<dt>p.rubric {</dt>
<dd>font-weight: bold ;
font-size: larger ;
color: maroon ;
text-align: center }</dd>
<dt>p.sidebar-title {</dt>
<dd>font-family: sans-serif ;
font-weight: bold ;
font-size: larger }</dd>
<dt>p.sidebar-subtitle {</dt>
<dd>font-family: sans-serif ;
font-weight: bold }</dd>
<dt>p.topic-title {</dt>
<dd>font-weight: bold }</dd>
<dt>pre.address {</dt>
<dd>margin-bottom: 0 ;
margin-top: 0 ;
font: inherit }</dd>
<dt>pre.literal-block, pre.doctest-block, pre.math, pre.code {</dt>
<dd>margin-left: 2em ;
margin-right: 2em }</dd>
</dl>
<p>pre.code .ln { color: grey; } /* line numbers <a href="#id17"><span class="problematic" id="id18">*</span></a>/
pre.code, code { background-color: #eeeeee }
pre.code .comment, code .comment { color: #5C6576 }
pre.code .keyword, code .keyword { color: #3B0D06; font-weight: bold }
pre.code .literal.string, code .literal.string { color: #0C5404 }
pre.code .name.builtin, code .name.builtin { color: #352B84 }
pre.code .deleted, code .deleted { background-color: #DEB0A1}
pre.code .inserted, code .inserted { background-color: #A3D289}</p>
<div class="system-message" id="id17">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 278); <em><a href="#id18">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<dl class="docutils">
<dt>span.classifier {</dt>
<dd>font-family: sans-serif ;
font-style: oblique }</dd>
<dt>span.classifier-delimiter {</dt>
<dd>font-family: sans-serif ;
font-weight: bold }</dd>
<dt>span.interpreted {</dt>
<dd>font-family: sans-serif }</dd>
<dt>span.option {</dt>
<dd>white-space: nowrap }</dd>
<dt>span.pre {</dt>
<dd>white-space: pre }</dd>
<dt>span.problematic {</dt>
<dd>color: red }</dd>
<dt>span.section-subtitle {</dt>
<dd><p class="first">/* font-size relative to parent (h1..h6 element) <a href="#id19"><span class="problematic" id="id20">*</span></a>/
font-size: 80% }</p>
<div class="last system-message" id="id19">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 308); <em><a href="#id20">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
</dd>
<dt>table.citation {</dt>
<dd>border-left: solid 1px gray;
margin-left: 1px }</dd>
<dt>table.docinfo {</dt>
<dd>margin: 2em 4em }</dd>
<dt>table.docutils {</dt>
<dd>margin-top: 0.5em ;
margin-bottom: 0.5em }</dd>
<dt>table.footnote {</dt>
<dd>border-left: solid 1px black;
margin-left: 1px }</dd>
</dl>
<p>table.docutils td, table.docutils th,
table.docinfo td, table.docinfo th {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 328)</p>
Unexpected indentation.</div>
<blockquote>
padding-left: 0.5em ;
padding-right: 0.5em ;
vertical-align: top }</blockquote>
<dl class="docutils">
<dt>table.docutils th.field-name, table.docinfo th.docinfo-name {</dt>
<dd>font-weight: bold ;
text-align: left ;
white-space: nowrap ;
padding-left: 0 }</dd>
</dl>
<p>/* &quot;booktabs&quot; style (no vertical lines) <a href="#id21"><span class="problematic" id="id22">*</span></a>/
table.docutils.booktabs {</p>
<div class="system-message" id="id21">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 338); <em><a href="#id22">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 340)</p>
Unexpected indentation.</div>
<blockquote>
border: 0px;
border-top: 2px solid;
border-bottom: 2px solid;
border-collapse: collapse;</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 344)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>}
table.docutils.booktabs * {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 346)</p>
Unexpected indentation.</div>
<blockquote>
border: 0px;</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 347)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>}
table.docutils.booktabs th {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 349)</p>
Unexpected indentation.</div>
<blockquote>
border-bottom: thin solid;
text-align: left;</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">output3.rst</tt>, line 351)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>}</p>
<p>h1 tt.docutils, h2 tt.docutils, h3 tt.docutils,
h4 tt.docutils, h5 tt.docutils, h6 tt.docutils {</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">output3.rst</tt>, line 355)</p>
Unexpected indentation.</div>
<blockquote>
font-size: 100% }</blockquote>
<dl class="docutils">
<dt>ul.auto-toc {</dt>
<dd>list-style-type: none }</dd>
</dl>
<p>&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class=&quot;document&quot;&gt;</p>
<p>&lt;p&gt;&amp;lt;!DOCTYPE html&amp;gt;
&amp;lt;html lang=&amp;quot;en&amp;quot;&amp;gt;&lt;/p&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: ERROR/3 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 3)&lt;/p&gt;
Unexpected indentation.&lt;/div&gt;
&lt;blockquote&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;head&amp;gt;&lt;/dt&gt;
&lt;dd&gt;&amp;lt;meta charset=&amp;quot;utf-8&amp;quot; /&amp;gt;
&amp;lt;title&amp;gt;KM Plumbing&amp;lt;/title&amp;gt;
&amp;lt;link rel=&amp;quot;stylesheet&amp;quot; href=&amp;quot;style.css&amp;quot;/&amp;gt;&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 7)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/head&amp;gt;
&amp;lt;body&amp;gt;&lt;/p&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: ERROR/3 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 9)&lt;/p&gt;
Unexpected indentation.&lt;/div&gt;
&lt;blockquote&gt;
&lt;p&gt;&amp;lt;div class=&amp;quot;wrapper&amp;quot;&amp;gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;&amp;lt;h1 id= &amp;quot;owner&amp;quot;&amp;gt;Keith McDonald Plumbing&amp;lt;/h1&amp;gt;&lt;/p&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;ul&amp;gt;&lt;/dt&gt;
&lt;dd&gt;&amp;lt;li&amp;gt;Installation &amp;amp;amp; Service of Septic Tanks &amp;amp;amp; Sewer Systems&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;Water Heater Installation &amp;amp;amp; Repair&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;Drain Cleaning&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;Plumbing for New Construction and Remodels&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;Pipe &amp;amp;amp; Leak Repair&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;Sewer Jetting&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;Video Camera Line Inspection&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;Portable Toilet Rental&amp;lt;/li&amp;gt;&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 23)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/ul&amp;gt;
&amp;lt;h3&amp;gt;Irrigation Installation Irrigation Installation and Service&amp;lt;/h3&amp;gt;&lt;/p&gt;
&lt;p&gt;&amp;lt;p&amp;gt;
Leaky pipes? Stopped up toilets? Full Septic Tanks?
&amp;lt;img id=&amp;quot;pipe&amp;quot; src=&amp;quot;img/pipe-leaking.jpg&amp;quot; alt=&amp;quot;Leaky Pipe&amp;quot; /&amp;gt;
&amp;lt;/p&amp;gt;&lt;/p&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;p&amp;gt;If so, call &amp;lt;span class=&amp;quot;name&amp;quot;&amp;gt;Keith McDonald Plumbing&amp;lt;/span&amp;gt;, Sewer &amp;amp;amp; Septic. We operate primarily&lt;/dt&gt;
&lt;dd&gt;in Washington, Baldwin, and Laurens Counties and surrounding middle Georgia.
Plumbing is our specialty and we have a staff of qualified technicians that
can quickly respond to your needs. We can handle jobs of any size. We have
an impressive resume that includes many large projects in the areas of
residential, commercial, educational, and medical. Visit our Projects
page for a sample of some of these jobs.&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 38)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/p&amp;gt;&lt;/p&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;p&amp;gt;At &amp;lt;span class=&amp;quot;name&amp;quot;&amp;gt;Keith McDonald Plumbing&amp;lt;/span&amp;gt;, Sewer &amp;amp;amp; Septic, we are dedicated to our promise&lt;/dt&gt;
&lt;dd&gt;of &amp;lt;em&amp;gt;&amp;quot;Quality, Dependable Service.&amp;quot;&amp;lt;/em&amp;gt; Our staff works very hard to see that
each customer, large or small, is satisfied with a job well done. We are
proud of the reputation that we have achieved and strive daily to maintain
that reputation. We want to be the first name you think of when you
have a plumbing need.&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 46)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/p&amp;gt;&lt;/p&gt;
&lt;p&gt;&amp;lt;p&amp;gt;&amp;lt;strong&amp;gt;&amp;lt;span class=&amp;quot;contact&amp;quot;&amp;gt;Contact us today.&amp;lt;/span&amp;gt;&amp;lt;/strong&amp;gt; We're looking forward to hearing from you!
&amp;lt;/p&amp;gt;&lt;/p&gt;
&lt;p&gt;&amp;lt;h3&amp;gt;General Plumbing Service Professionals - &amp;lt;em&amp;gt;LICENSED &amp;amp;amp; INSURED&amp;lt;/em&amp;gt;
&amp;lt;/h3&amp;gt;&lt;/p&gt;
&lt;p&gt;&amp;lt;h4&amp;gt;Proud Member of:&amp;lt;/h4&amp;gt;
&amp;lt;ul&amp;gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;&amp;lt;li&amp;gt;&amp;lt;a href=&amp;quot;&lt;a class=&quot;reference external&quot; href=&quot;http://www.washingtoncountyga.com/&quot;&gt;http://www.washingtoncountyga.com/&lt;/a&gt;&amp;quot; target=&amp;quot;_blank&amp;quot;&amp;gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;figure&amp;gt;&lt;/dt&gt;
&lt;dd&gt;&lt;p class=&quot;first&quot;&gt;&amp;lt;img src=&amp;quot;img/washington-county.png&amp;quot; alt=&amp;quot;Washington County Chamber of Commerce&amp;quot; /&amp;gt;
&amp;lt;figcaption&amp;gt;&lt;/p&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: ERROR/3 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 62)&lt;/p&gt;
Unexpected indentation.&lt;/div&gt;
&lt;blockquote&gt;
Washington County Chamber of Commerce&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 63)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p class=&quot;last&quot;&gt;&amp;lt;/figcaption&amp;gt;&lt;/p&gt;
&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 64)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/figure&amp;gt;
&amp;lt;/a&amp;gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 66)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/li&amp;gt;
&amp;lt;li&amp;gt;&amp;lt;a href=&amp;quot;&lt;a class=&quot;reference external&quot; href=&quot;http://www.wilcodevauthority.com/chamber/index2.php&quot;&gt;http://www.wilcodevauthority.com/chamber/index2.php&lt;/a&gt;&amp;quot; target=&amp;quot;_blank&amp;quot;&amp;gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;figure&amp;gt;&lt;/dt&gt;
&lt;dd&gt;&lt;p class=&quot;first&quot;&gt;&amp;lt;img src=&amp;quot;img/wilkinson.png&amp;quot; alt=&amp;quot;Wilkinson County Georgia Chamber of Commerce&amp;quot; /&amp;gt;
&amp;lt;figcaption&amp;gt;&lt;/p&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: ERROR/3 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 72)&lt;/p&gt;
Unexpected indentation.&lt;/div&gt;
&lt;blockquote&gt;
Wilkinson County Georgia Chamber of Commerce&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 73)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p class=&quot;last&quot;&gt;&amp;lt;/figcaption&amp;gt;&lt;/p&gt;
&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 74)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/figure&amp;gt;
&amp;lt;/a&amp;gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 76)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/li&amp;gt;&lt;/p&gt;
&lt;p&gt;&amp;lt;li&amp;gt;&amp;lt;a href=&amp;quot;&lt;a class=&quot;reference external&quot; href=&quot;http://milledevillega.com/&quot;&gt;http://milledevillega.com/&lt;/a&gt;&amp;quot; target=&amp;quot;_blank&amp;quot;&amp;gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;figure&amp;gt;&lt;/dt&gt;
&lt;dd&gt;&lt;p class=&quot;first&quot;&gt;&amp;lt;img src=&amp;quot;img/baldwin-county.png&amp;quot; alt=&amp;quot;Baldwin County Chamber of Commerce&amp;quot; /&amp;gt;
&amp;lt;figcaption&amp;gt;&lt;/p&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: ERROR/3 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 83)&lt;/p&gt;
Unexpected indentation.&lt;/div&gt;
&lt;blockquote&gt;
Baldwin County Chamber of Commerce&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 84)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p class=&quot;last&quot;&gt;&amp;lt;/figcaption&amp;gt;&lt;/p&gt;
&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 85)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/figure&amp;gt;
&amp;lt;/a&amp;gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 87)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/li&amp;gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 88)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/ul&amp;gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;dl class=&quot;docutils&quot;&gt;
&lt;dt&gt;&amp;lt;section id=&amp;quot;myCopy&amp;quot;&amp;gt;&lt;/dt&gt;
&lt;dd&gt;&amp;lt;h5&amp;gt;&amp;amp;copy; Site operated by Aspasia Karfakis &amp;lt;/h5&amp;gt;
&amp;lt;h4&amp;gt;Keith McDonald Plumbing&amp;lt;/h4&amp;gt;&lt;/dd&gt;
&lt;/dl&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 93)&lt;/p&gt;
Definition list ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/section&amp;gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;p&gt;&amp;lt;/div&amp;gt;&amp;lt;!-- END WRAPPER --&amp;gt;&lt;/p&gt;
&lt;/blockquote&gt;
&lt;div class=&quot;system-message&quot;&gt;
&lt;p class=&quot;system-message-title&quot;&gt;System Message: WARNING/2 (&lt;tt class=&quot;docutils&quot;&gt;index.htm&lt;/tt&gt;, line 96)&lt;/p&gt;
Block quote ends without a blank line; unexpected unindent.&lt;/div&gt;
&lt;p&gt;&amp;lt;/body&amp;gt;
&amp;lt;/html&amp;gt;&lt;/p&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</p>
</div>
</body>
</html>
