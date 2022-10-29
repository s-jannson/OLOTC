import Vue from 'vue';
import * as echarts from 'echarts'

// import ECharts modules manually to reduce bundle size
// import 'echarts/lib/chart/bar'
// import 'echarts/lib/component/tooltip'

// register component to use
Vue.component('Chart', echarts);
