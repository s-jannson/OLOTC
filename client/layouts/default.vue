<template lang="pug">
  //- nav.navbar.header.has-shadow.is-primary(role='navigation', aria-label='main navigation')
  //-   .navbar-brand
  //-     a.navbar-item(href='/')
  //-       img(src='~assets/buefy.png', alt='Buefy', height='28')
  //-     .navbar-burger
  //-       span
  //-         span
  //-           span
  //- section.main-content.columns
  //-   aside.column.is-2.section
  //-     p.menu-label.is-hidden-touch General
  //-     ul.menu-list
  //-       li(v-for='(item, key) of items', :key='key')
  //-         nuxtlink(:to='item.to', exact-active-class='is-active')
  //-           b-icon(:icon='item.icon')
  div
    nuxt
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      items: [
        {
          title: 'Home',
          icon: 'home',
          to: { name: 'index' },
        },
        {
          title: 'Inspire',
          icon: 'lightbulb',
          to: { name: 'inspire' },
        },
      ],
    }
  },
}
</script>
