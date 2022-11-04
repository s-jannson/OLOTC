<template lang="pug">
.column
  .card
    .card-content
      .content.has-text-centered
        h2 🚨 Last reported price: ${{price}} at {{printDate(date)}} 🚨
</template>

<script>
export default {
  name: 'LastReport',
  props: {
    price: {
      type: Number,
      required: true,
    },
    date: {
      type: Date,
      required: true,
    },
  },
  methods: {
    printDate(dateInput) {
      const dateStr =
        this.padStr(dateInput.getFullYear()) +
        '-' +
        this.padStr(1 + dateInput.getMonth()) +
        '-' +
        this.padStr(dateInput.getDate())
      return dateStr
    },
    padStr(i) {
      return i < 10 ? '0' + i : '' + i
    },
  },
}
</script>
<style lang="scss" scoped>
.column {
  padding: 0.75rem 0;
}
</style>
