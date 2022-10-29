<template lang="pug">
  section.section
    section.hero.is-medium.is-primary.is-bold
      .hero-body
        .container
          h1.title 0L OTC price discovery
          h2.subtitle Independent and unaffiliated price discovery tool for the 0L OTC market
          h3.subtitle.italic
            br
            | Please don't report fake information.
            br
            | The community is relying on valid data coming from such tools, to
            | make informed decisions and payments from community wallets to contributors
    LastReport(price='0.05', date='2022-10-22 00:00:00')
    //- LastReport(:price='0.05', :date='')
    TradeHistoryChart
</template>

<script>
import LastReport from '~/components/LastReport'
import TradeHistoryChart from '~/components/TradeHistoryChart'

export default {
  name: 'IndexPage',
  components: {
    LastReport,
    TradeHistoryChart,
  },
}
</script>
<style lang="scss" scoped>
.italic {
  font-style: italic;
}
</style>
