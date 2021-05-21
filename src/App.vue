<template>
  <div id="app" class="grid-container">
    <div class="grid-item">
      <h3>Chapters</h3>
        <a v-for="(chapter, index) in textbookChapters" :key="index" @click="changeChapter(index)"><ul style="font-size: xx-small">{{ chapter }}</ul></a>
    </div>
    <PDFJSViewer class="grid-item" :path="`${path}`" :fileName="`${name}`"/>
  </div>
</template>

<script>
import PDFJSViewer from './components/PDFJSViewer'
import textbookChapters from '.././public/lib/web/textbook/output.json'

export default {
  name: 'app',
  components: {
    PDFJSViewer
  },
  data () {
    return {
      name: 'textbook/Chapter-1---Innovation-S-Curves-in-Living-Drug_2020_Second-Generation-Cell-a.pdf', //change which pdf file loads
      textbookChapters: textbookChapters,
      path: 'lib/web/viewer.html' //path of the PDF.js viewer.html
    }
  },
  methods: {
    changeChapter: function(index){
      this.name = "textbook/" + textbookChapters[index];
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.grid-container {
  display: grid;
  grid-template-columns: 200px auto;
}
</style>
