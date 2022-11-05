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
    //- LastReport(price='0.05', date='2022-10-22 00:00:00')
    div(v-if="tradesFromDb")
      LastReport(:price="tradesFromDb[tradesFromDb.length-1].price_usd" , :date="new Date(tradesFromDb[tradesFromDb.length-1].datetime)")
      TradeHistoryChart(:trades="tradesFromDb")
    TradeReport
    Todo
</template>

<script>
import LastReport from '~/components/LastReport'
import TradeHistoryChart from '~/components/TradeHistoryChart'
import TradeReport from '~/components/TradeReport'
import Todo from '~/components/Todo'

export default {
  name: 'IndexPage',
  components: {
    LastReport,
    TradeHistoryChart,
    TradeReport,
    Todo,
  },
  async asyncData({ $axios }) {
    const tradesFromDb = await $axios.$get('https://olotc.xyz/api/')
    if (tradesFromDb.length > 0) {
      return { tradesFromDb }
    }
  },
}
</script>
<style lang="scss" scoped>
.italic {
  font-style: italic;
}
</style>
