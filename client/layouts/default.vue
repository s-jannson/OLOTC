<template lang="pug">
div
  nuxt
  footer.footer
    .content.has-text-centered
      p
        strong OLOTC
        |  | View code on
        a(href='https://github.com/s-jannson/OLOTC', target="_blank")  Github
        |  (and do feel free to improve and open PRs)
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
