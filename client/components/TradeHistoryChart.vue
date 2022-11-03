<template lang="pug">
section.section
  .column
    .card
      .card-content
        .content.has-text-centered
          v-chart.chart(:option='optionScatter', autoresize)
          //- chart(:options="tradesChart",
          //-       autoresize,
          //-       ref="tradesChart")
</template>
<script>
import { format } from 'date-fns'
import { use, graphic } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { ScatterChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent } from 'echarts/components'
import VChart from 'vue-echarts'
// import { THEME_KEY } from 'vue-echarts'

use([CanvasRenderer, ScatterChart, TitleComponent, TooltipComponent])

export default {
  name: 'TradeHistoryChart',
  components: {
    VChart,
  },
  provide: {
    // [THEME_KEY]: 'dark',
  },
  data() {
    const tradesData = [
      {
        datetime: 'Sat, 15 Aug 2022 00:00:00 GMT',
        price_usd: 0.03,
        quantity: 17000.0,
        total_value: 2960.0,
      },
      {
        datetime: 'Sun, 03 Sep 2022 00:00:00 GMT',
        price_usd: 0.05,
        quantity: 20000.0,
        total_value: 1000.0,
      },
      {
        datetime: 'Sat, 18 Sep 2021 00:00:00 GMT',
        price_usd: 0.06,
        quantity: 25000.0,
        total_value: 2960.0,
      },
      {
        datetime: 'Sun, 02 Oct 2022 00:00:00 GMT',
        price_usd: 0.06,
        quantity: 50000.0,
        total_value: 1000.0,
      },
      {
        datetime: 'Sat, 08 Oct 2021 00:00:00 GMT',
        price_usd: 0.065,
        quantity: 70000.0,
        total_value: 2960.0,
      },
      {
        datetime: 'Sun, 21 Oct 2022 00:00:00 GMT',
        price_usd: 0.07,
        quantity: 300000.0,
        total_value: 1000.0,
      },
    ]

    // tradesData.map(Object.values)
    const tradesData2 = [
      ['2022-08-15T00:00:00.000Z', 0.03, 17000, 2960],
      ['2022-09-03T00:00:00.000Z', 0.05, 20000, 1000],
      ['2021-09-18T00:00:00.000Z', 0.06, 25000, 2960],
      ['2022-10-02T00:00:00.000Z', 0.06, 50000, 1000],
      ['2021-10-08T00:00:00.000Z', 0.065, 70000, 2960],
      ['2022-10-21T00:00:00.000Z', 0.07, 300000, 1000],
    ]

    const dollarUSLocale = Intl.NumberFormat('en-US')

    return {
      optionPie: {
        title: {
          text: 'Traffic Sources',
          left: 'center',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)',
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: [
            'Direct',
            'Email',
            'Ad Networks',
            'Video Ads',
            'Search Engines',
          ],
        },
        series: [
          {
            name: 'Traffic Sources',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: [
              { value: 335, name: 'Direct' },
              { value: 310, name: 'Email' },
              { value: 234, name: 'Ad Networks' },
              { value: 135, name: 'Video Ads' },
              { value: 1548, name: 'Search Engines' },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
              },
            },
          },
        ],
      },
      optionScatter: {
        backgroundColor: new graphic.RadialGradient(0.3, 0.3, 0.8, [
          {
            offset: 0,
            color: '#f7f8fa',
          },
          {
            offset: 1,
            color: '#cdd0d5',
          },
        ]),
        title: {
          text: 'Trades history',
          // subtext: 'Red bubble = trade size\nPurple bubble = total value',
          subtext: 'Bubble size = Total value',
          left: 'center',
          top: '5%',
          textStyle: {
            fontSize: 25,
          },
          subtextStyle: {
            fontSize: 18,
          },
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross',
          },
          formatter: function (params) {
            return `${dollarUSLocale.format(params.data[2])} coins @ $${
              params.data[1]
            }<br>
                    Total value: $${dollarUSLocale.format(params.data[3])}`
          },
        },
        grid: {
          left: '8%',
          top: '10%',
        },
        xAxis: {
          type: 'category',
          splitLine: {
            lineStyle: {
              type: 'dashed',
            },
          },
          axisLabel: {
            formatter: function (value) {
              return format(new Date(value), 'yyyy-MM-dd HH:mm:ss')
            },
          },
        },
        yAxis: {
          type: 'value',
          splitLine: {
            lineStyle: {
              type: 'dashed',
            },
          },
          scale: true,
        },
        dataset: {
          source: tradesData2,
          dimensions: ['timestamp', 'price', 'size', 'totalValue'],
        },
        series: [
          {
            name: 'price',
            type: 'line',
            lineStyle: {
              color: 'rgb(4, 31, 199)',
            },
            encode: {
              x: 'timestamp',
              y: 'price',
            },
            symbolSize: 0,
          },
          {
            name: 'tradeValue',
            type: 'scatter',
            encode: {
              x: 'timestamp',
              y: 'price',
            },
            symbolSize: function (data) {
              return Math.sqrt(data[3])
            },
            itemStyle: {
              shadowBlur: 10,
              shadowColor: 'rgba(120, 36, 50, 0.5)',
              shadowOffsetY: 5,
              color: new graphic.RadialGradient(0.4, 0.3, 1, [
                {
                  offset: 0,
                  color: 'rgb(251, 118, 123)',
                },
                {
                  offset: 1,
                  color: 'rgb(204, 46, 72)',
                },
              ]),
            },
          },
        ],
      },
    }
  },
}
</script>
<style lang="scss" scoped>
.section {
  padding: 0;
}

.card-content {
  padding: 0;
}

.column {
  padding: 0.75rem 0;
}

.chart {
  height: 100vh;
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
