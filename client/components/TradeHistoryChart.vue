<template lang="pug">
.column
  .card
    .card-content
      .content.has-text-centered
        square(v-if="isLoading", height=100, width=100, color='#7050D5')
  //- chart(:options="PerformanceChart",
  //-       autoresize,
  //-       ref="PerformanceChart",
  //-       @legendselectchanged="legendChange")

  //- .box(v-if="noSingleSelected()") Can't present single data series when no single portfolio has been selected...
  //- div(v-else)
  //-   nav.panel(v-if="this.$store.getters['app/isSinglePortfolioView']")
  //-     p.panel-heading Performance
  //-     .panel-block
  //-       chart(:options="PerformanceChart",
  //-             autoresize,
  //-             ref="PerformanceChart",
  //-             @legendselectchanged="legendChange")
  //-   chart(v-else,
  //-         :options="PerformanceChart",
  //-         autoresize,
  //-         ref="PerformanceChart",
  //-         @legendselectchanged="legendChange")

</template>
<script>
// import square from 'vue-spinner/src/RingLoader.vue'
// import ECharts from 'vue-echarts/components/ECharts.vue'
// import 'echarts/lib/chart/line'
// import 'echarts/lib/component/title'
// import 'echarts/lib/component/legendScroll'
// import 'echarts/lib/component/tooltip'
// import 'echarts/lib/component/toolbox/feature/SaveAsImage.js'
// import 'echarts/lib/component/brush.js'
// import 'echarts/lib/component/dataZoom.js'
// import 'echarts/lib/component/dataZoomInside.js'
// import 'echarts/lib/component/legend'
export default {
  components: {
    // RingLoader,
    // chart: ECharts,
  },
  data() {
    // const store = this.$store
    return {
      isLoading: true,
      PerformanceChart: {
        title: {
          text: '',
        },
        toolbox: {
          itemSize: 20,
          feature: {
            saveAsImage: {
              title: 'Save Image',
            },
          },
        },
        grid: {
          left: '5%',
          right: '2%',
          bottom: '40%',
          // right: store.getters['app/isSinglePortfolioView'] ? '2%' : '20%',
          // bottom: store.getters['app/isSinglePortfolioView'] ? '40%' : '8%',
          containLabel: true,
        },
        yAxis: [
          {
            type: 'value',
          },
        ],
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: [],
            bottom: 0,
          },
        ],
        // dataZoom: [
        //   {
        //     type: 'slider',
        //     show: true,
        //     xAxisIndex: [0],
        //     start: 0,
        //     end: 100,
        //     bottom: store.getters['app/isSinglePortfolioView'] ? 60 : 0,
        //   },
        //   {
        //     type: 'inside',
        //     start: 0,
        //     end: 100,
        //   },
        // ],
      },
    }
  },
  // computed: {
  //   chartData() {
  //     return this.$store.getters['app/chartData']
  //   },
  //   chartDates() {
  //     return this.$store.getters['app/chartDates']
  //   },
  // },
  // async mounted() {
  //   if (!this.noSingleSelected()) {
  //     this.updateRunChart()
  //   }

  //   setTimeout(() => {
  //     window.onresize = function () {
  //       // eslint-disable-next-line no-undef
  //       if (this.$refs && PerformanceChart in this.$refs) {
  //         const refsChart = this.$refs.PerformanceChart
  //         if (refsChart) {
  //           refsChart.resize()
  //         }
  //       }
  //     }
  //   }, 3000)
  // },
  methods: {
    // noSingleSelected() {
    //   return (
    //     this.$store.getters['app/isSinglePortfolioView'] &&
    //     !this.$store.getters['app/chartData']
    //   )
    // },
    // legendChange(playerLegend) {
    //   const portfolioId = this.chartData.filter(
    //     (x) => x.name === playerLegend.name
    //   )[0].portfolio_id
    //   this.$store.commit('app/SET_SINGLE_PORTFOLIO_ID', portfolioId)
    //   this.$store.commit('app/SET_SINGLE_PORTFOLIO_NAME', playerLegend.name)
    //   this.$store.commit('app/SINGLE_TRUE')
    //   this.$router.push({ path: 'single' })
    // },
    // updateRunChart() {
    //   const store = this.$store
    //   const that = this
    //   const preparedData = {
    //     tooltip: (function () {
    //       if (!store.getters['app/isSinglePortfolioView']) {
    //         return {
    //           trigger: 'axis',
    //           formatter: function (v) {
    //             function sortData(a, b) {
    //               return b.data - a.data
    //             }
    //             v.sort(sortData)
    //             let tempStr = ''
    //             for (const i in v) {
    //               tempStr += `<tr><td style=""><div style="width:10px;height:10px;background:${v[i].color}"></div></td><td><div style="font-size:14px;">${v[i].seriesName} => ${v[i].data}</div></td></tr>`
    //             }
    //             const html = `<table>${tempStr}</table>`
    //             return html
    //           },
    //           // eslint-disable-next-line no-unused-vars
    //           position: function (pt) {
    //             return ['10%', '10%']
    //           },
    //           confine: true,
    //           axisPointer: {
    //             type: 'cross',
    //             label: {
    //               backgroundColor: '#6a7985',
    //             },
    //           },
    //         }
    //       } else {
    //         return {
    //           trigger: 'axis',
    //           formatter: function (v) {
    //             if (
    //               store.getters['app/isSinglePortfolioView'] &&
    //               store.getters['app/hoveredDatetime'] !== v[0].name
    //             ) {
    //               store.commit('app/SET_HOVERED_DATETIME', v[0].name)
    //             }
    //           },
    //         }
    //       }
    //     })(),
    //     legend: (function () {
    //       if (store.getters['app/isSinglePortfolioView']) {
    //         return null
    //       } else {
    //         return {
    //           data: that.chartData.sort((a, b) => {
    //             return b.data[b.data.length - 1] - a.data[a.data.length - 1]
    //           }),
    //           selectedMode: 'multiple',
    //           right: '0%',
    //           top: '7%',
    //           orient: 'vertical',
    //           type: 'scroll',
    //         }
    //       }
    //     })(),
    //     xAxis: [
    //       {
    //         type: 'category',
    //         boundaryGap: false,
    //         data: this.chartDates,
    //         bottom: 0,
    //       },
    //     ],
    //     series: that.chartData,
    //   }
    //   that.$refs.PerformanceChart.mergeOptions(preparedData)
    // },
  },
}
</script>
<style lang="scss" scoped>
.column {
  padding: 0.75rem 0;
}
// @import '@/assets/scss/style.scss';
.panel {
  border-radius: 5px;
}
.panel-heading {
  // background-color: $panel-heading-color;
  color: white;
  border-radius: 10px 10px 0px 0px;
}
.panel-block:last-of-type {
  border-radius: 0px 0px 10px 10px;
  // border-bottom: none;
  border-left: none !important;
  border-right: none !important;
}
</style>
