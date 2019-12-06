<template>
  <div class="wrapper">
    <side-bar>
      <template slot="links">
        <sidebar-link to="/marketplace" name="Acheter" icon="ti-shopping-cart"/>
        <sidebar-link to="/asset" name="Mes actifs" icon="ti-package"/>
        <sidebar-link to="/invoice" name="Mes factures" icon="ti-credit-card"/>
        <sidebar-link to="/documents" name="Mes documents" icon=""/> <!-- TODO Add logo-->
        
        <sidebar-link to="/ticket" name="Mes tickets" icon="ti-shopping-cart "/>
        <sidebar-link to="/event" name="Mes evenements" icon="ti-shopping-cart "/>
        <sidebar-link to="/calendar" name="Mes Calendriers" icon="ti-calendar"/>
        <sidebar-link to="/project" name="Mes Projets" icon="ti-shopping-cart "/>
        <sidebar-link to="/sc" name="Mes Contrats de Services" icon="ti-shopping-cart "/>
        <sidebar-link to="/permissions" name="Droits et roles" icon="ti-shopping-cart "/>
        <sidebar-link to="/faq" name="FAQ" icon="ti-shopping-cart "/>
        <sidebar-link to="/s6" name="Visualiser ma salle" icon="ti-shopping-cart "/>
      </template>
    </side-bar>
    <div class="main-panel">
      <top-bar />
      <page-content @click.native="toggleSidebar" />
      <page-footer />
    </div>
  </div>
</template>
<style lang="scss">
</style>
<script>
import TopBar from "./TopBar.vue";
import PageFooter from "./PageFooter.vue";
import PageContent from "./PageContent.vue";
export default {
  components: {
    PageFooter,
    PageContent,
    TopBar,
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  }
};
</script>
