<template lang="pug">
.column
  .card
    .card-content
      .content.has-text-centered
        h2 🚨 Last reported price: ${{price}} at {{date}} 🚨
        //- b-icon(:icon='icon', size='is-large', type='is-primary')
</template>

<script>
export default {
  name: 'LastReport',
  props: {
    price: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
  },
}
</script>
<style lang="scss" scoped>
.column {
  padding: 0.75rem 0;
}
</style>
