<template lang="pug">
section.section
  .column
    .card
      .card-content
        .container
          .content.has-text-centered
            .title Submit new OTC trade
            b-field(grouped, group-multiline)
              b-input(v-model='amount', type='number', min='0', step="any", placeholder='GAS amount sold')
              b-input(v-model='price', type='number', min='0', step="any", placeholder='Price per coin ($)')
              b-datetimepicker(
                v-model='selectedDatetime',
                placeholder='Click to select datetime',
                icon='calendar-today',
                :icon-right="selectedDatetime ? 'close-circle' : ''",
                icon-right-clickable,
                @icon-right-click='clearDateTime',
                :locale='locale',
                :first-day-of-week='firstDayOfWeek',
                :datepicker='{ showWeekNumber }',
                :timepicker='{ enableSeconds, hourFormat }',
                horizontal-time-picker)

              b-button(type='is-primary', outlined, @click="submitTrade") Submit
</template>
<script>
export default {
  name: 'TradeReport',
  data() {
    return {
      amount: null,
      price: null,
      selectedDatetime: null,
      showWeekNumber: false,
      enableSeconds: false,
      hourFormat: undefined, // Browser locale
      locale: undefined, // Browser locale
      firstDayOfWeek: undefined, // 0 - Sunday
    }
  },
  methods: {
    clearDateTime() {
      this.selectedDatetime = null
    },
    async submitTrade() {
      if (this.amount && this.price && this.selectedDatetime) {
        const trade = {
          quantity: this.amount,
          price: this.price,
          datetime: this.selectedDatetime,
        }
        const res = await this.$axios.$post('http://localhost:5000/new', trade)
        if (res === 'ok') {
          this.$buefy.toast.open({
            message: 'Trade submitted successfully! Thank you!',
            type: 'is-success',
            duration: 5000,
          })
        } else {
          this.$buefy.toast.open({
            message: 'Trade submission failed!',
            type: 'is-danger',
            duration: 5000,
          })
        }
      }
    },
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

.container {
  padding: 3rem;
}

.column {
  padding: 0.75rem 0;
}
</style>
