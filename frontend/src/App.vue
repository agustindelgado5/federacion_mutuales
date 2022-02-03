<template>
  <v-app>
    <v-breadcrumbs :items="items" divider="|">
      <template v-slot:item="{ item }">
        <v-breadcrumbs-item :to="item.to" :disabled="item.disabled">
          {{ item.text }}
        </v-breadcrumbs-item>
      </template>
    </v-breadcrumbs>
    <sidebar-menu
      :menu="menu"
      id="menulo"
      ref="menulo"
      :show-child="false"
      :collapsed="true"
      :theme="selectedTheme"
    >
      <template v-slot:header>
        <input
            type="text"
            id="buscadorepico"
            v-on:keyup="buscarnow()"
            class="buscador"
            ref="buscadormenu"
            placeholder="Buscar Acciones..."
            style="background-color:black;"
        />
      </template>
      <template v-slot:toggle-icon> </template>
      <template v-slot:dropdown-icon="{ isOpen }">
        <span v-if="!isOpen">+</span>
        <span v-else>-</span>
      </template>
    </sidebar-menu>

    <!--<div class="Menu">

        <MenuBurger :handleBurgerClicked="clickBurger" class="botondemenu" />

        <MenuShadow :isActive="isActive" :handleShadowClicked="clickShadow" />

        <div class="Menu__panel-wrapper"
             :class="{'isActive': isActive}"
             :style="[style_wrapperStyle, isActive ? style_wrapperActiveStyle : {}]">

            <MenuPanel :list="content_prevItem"
                       :functionalityStyle="style_panelStyle"
                       :positionStyle="panel_prevPositionStyle"
                       :isTranslating="isTranslating"
                       :transitionStyle="style_transitionStyle"
                       :showHeaderArrow="prevItemHasParent" />

            <MenuPanel :list="content_currentItem"
                       :functionalityStyle="style_panelStyle"
                       :positionStyle="panel_stagingPositionStyle"
                       :isTranslating="isTranslating"
                       :transitionStyle="style_transitionStyle"
                       :showHeaderArrow="currentItemHasParent"
                       :handleHeaderClicked="clickPrevItem"
                       :handleItemClicked="clickNextItem" />

            <MenuPanel :list="content_nextItem"
                       :functionalityStyle="style_panelStyle"
                       :positionStyle="panel_nextPositionStyle"
                       :isTranslating="isTranslating"
                       :transitionStyle="style_transitionStyle"
                       :showHeaderArrow="true" />
        </div>

    </div>-->
    <v-main>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
import demoData from "./infomenu.js";

import functionalityStyle from "./mixins/functionalityStyle.mixin";
import panelControl from "./mixins/panelControl.mixin";
import contentControl from "./mixins/contentControl.mixin";

import RightArrowIcon from "./icons/RightArrowIcon.vue";
import LeftArrowIcon from "./icons/LeftArrowIcon.vue";
import MenuBurger from "./components/MenuBurger.vue";
import MenuShadow from "./components/MenuShadow.vue";
import MenuPanel from "./components/MenuPanel.vue";

export default {
  mixins: [functionalityStyle, panelControl, contentControl],
  components: {
    RightArrowIcon,
    LeftArrowIcon,
    MenuBurger,
    MenuShadow,
    MenuPanel,
  },
  props: {
    source: {
      type: Object,
      default: () => demoData,
    },
    panelWidth: {
      type: Number,
      default: 300,
    },
    menuOpenSpeed: {
      type: Number,
      default: 350,
    },
    menuSwitchSpeed: {
      type: Number,
      default: 300,
    },
    width: {
      type: String,
      default: "350px",
    },
  },
  created() {
    console.log(process.env.VUE_APP_API_HOST, process.env.VUE_APP_API_PORT);
  },
  data() {
    return {
      items: [
        // {
        //   text: "Iniciar Sessión",
        //   disable: false,
        //   to: "/login",
        // },
        {
          text: "Servicios",
          disable: false,
          to: "/servicios",
        },
        {
          text: "Mutuales",
          disable: false,
          to: "/mutuales",
        },
        {
          text: "Socios",
          disable: false,
          to: "/socios",
        },
        {
          text: "Profesionales",
          disable: false,
          to: "/profesionales",
        },
        {
          text: "Farmacias",
          disable: false,
          to: "/farmacias",
        },
        {
          text: "Medicamentos",
          disable: false,
          to: "/medicamentos",
        },
        {
          text: "Recetas",
          disable: false,
          to: "/recetas",
        },
        {
          text: "Ordenes",
          disable: false,
          to: "/ordenes",
        },
        {
          text: "Cobradores",
          disable: false,
          to: "/cobradores",
        },
        {
          text: "Gastos",
          disable: false,
          to: "/gastosSalientes",
        },
        {
          text: "Cirugias",
          disable: false,
          to: "/cirugias",
        },
        {
          text: "Institutos",
          disable: false,
          to: "/institutos",
        },
        {
          text: "Lentes",
          disable: false,
          to: "/lentes",
        },
        {
          text: "Opticas",
          disable: false,
          to: "/ventasOpticas",
        },
      ],
      name: "SidebarMenu",
      menu: [
        {
          header: `Federacion de Mutuales`,
          hiddenOnCollapse: true,
        },
        {
          title: `Inicio`,
          href: `/`,
          icon: "fa fa-home",
          child: [],
        },
        {
          title: `Usuarios`,
          href: `/socios`,
          icon: "fa fa-user",
          child: [],
        },
        {
          title: `Socios`,
          href: "/socios",
          icon: "fa fa-id-badge",
          child: [],
        },
        {
          title: `Profesionales`,
          href: "/profesionales",
          icon: "fa fa-briefcase-medical",
          child: [],
        },
        {
          title: `Cobradores`,
          href: "/cobradores",
          icon: "fa fa-money-bill",
          child: [],
        },
        {
          title: `Salud`,
          icon: "fa fa-hand-holding-medical",
          child: [
            {
              title: `Ordenes Medicas`,
              href: "/ordenes",
              child: [],
            },
            {
              title: `Institutos`,
              href: "/institutos",
              child: [],
            },
            {
              title: `Estudios`,
              href: "/estudios",
              child: [
                {
                  title: `Imagenes`,
                  href: `/`,
                  child: [],
                },
                {
                  title: `Analisis Bioquimicos`,
                  href: `/`,
                  child: [],
                },
              ],
            },
            {
              title: `Cirugias`,
              href: "/cirugias",
              child: [],
            },
          ],
        },
        {
          title: `Farmacias`,
          icon: "fa fa-pills",
          child: [
            {
              title: `Info Farmacias`,
              href: `/farmacias`,
              child: [],
            },
            {
              title: `Medicamentos`,
              href: `/medicamentos`,
              child: [],
            },
            {
              title: `Recetas`,
              href: `/recetas`,
              child: [],
            },
          ],
        },
        {
          title: `Registro Contable`,
          icon: "fa fa-dollar-sign",
          child: [
            {
              title: `Gastos Salientes`,
              href: `/gastosSalientes`,
              child: [],
            },
            {
              title: `Gastos Profesionales`,
              href: `/profesionales/list_pagos`,
              child: [],
            },
            {
              title: `Cuotas de Socios`,
              href: `/cuotas`,
              child: [],
            },
          ],
        },
        {
          title: `Mutuales`,
          href: "/mutuales",
          icon: "fa fa-clinic-medical",
          child: [],
        },
        {
          title: `Servicios`,
          href: "/servicios",
          icon: "fa fa-chart-pie",
          child: [],
        },
      ],
      selectedTheme: "dark-theme",
      isActive: false,
      isTranslating: false,
    };
  },
  mounted: function () {
    this.content_currentItem = this.source;
    // console.log(this.$refs.menuulo);
  },
  computed: {
    currentItemHasParent() {
      return this.content_parentStack.length >= 1;
    },
    prevItemHasParent() {
      return this.content_parentStack.length >= 2;
    },
  },
  watch: {
    list() {
      this.content_currentItem = this.source;
    },
  },
  methods: {
    clickBurger() {
      this.isActive = !this.isActive;
    },
    clickShadow() {
      this.isActive = false;
    },
    clickNextItem(targetItem) {
      if (this.isTranslating || targetItem.children.length <= 0) {
        return;
      }

      this.slideToNext(targetItem);
    },
    clickPrevItem() {
      if (this.isTranslating || !this.currentItemHasParent) {
        return;
      }

      this.slideToPrev();
    },
    async buscarnow() {
      // Declare variables
      var input, filter, ul, li, a, i, txtValue, menu;
      input = this.$refs.buscadormenu;
      filter = input.value.toUpperCase();
      menu = this.$refs.menulo;
      console.log(menu);
      li = menu.$el.getElementsByTagName("a");
      console.log(li);
      // Loop through all list items, and hide those who don't match the search query
      for (i = 0; i < li.length; i++) {
        //a = li[i].getElementsByTagName("a")[0];
        txtValue = li[i].textContent || li[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
        } else {
          li[i].style.display = "none";
        }
      }
    },
    /*
     * main part of core
     * definite of how to handle panel sliding and item updating
     */
    slideToNext(targetItem) {
      // set target item as content of next panel
      this.content_setNextItem(targetItem);

      // switch animation on
      this.setTranslating(true);

      // activate panel sliding with animation after `.translating` class has updated to panel dom.
      this.$nextTick(() => {
        this.panel_slideNext();
      });

      // reset panel position
      this.homingAfterTranslatingNext();
    },
    slideToPrev() {
      // set prev item which is the parent of the current item.
      this.content_setPrevItem();

      // switch animation on
      this.setTranslating(true);

      // activate panel sliding with animation after `.translating` class has updated to panel dom.
      this.$nextTick(() => {
        this.panel_slideBack();
      });

      // reset panel position
      this.homingAfterTranslatingBack();
    },

    // handle homing after slide animation end
    homingAfterTranslatingNext() {
      setTimeout(() => {
        // switch off transition state of panel
        this.setTranslating(false);

        // push current to parent stack
        this.content_pushCurrentToParentStack();

        // homing
        this.panel_homingPosition(); // reset panel position just like the beginning.
        this.content_homingItemAfterNext(); // change item between these panels to meet updated panel position.
      }, this.menuSwitchSpeed);
    },
    homingAfterTranslatingBack() {
      setTimeout(() => {
        this.setTranslating(false);

        // homing
        this.panel_homingPosition();
        this.content_homingItemAfterBack();
      }, this.menuSwitchSpeed);
    },

    // utils
    setTranslating(status) {
      this.isTranslating = status;
    },
  },
};
</script>
<style>
/* #buscadorepico {
  background-image: url("/assets/search.png");
  background-size: 8%;
  background-position: 10px 12px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  margin-bottom: 12px;
  padding-left: 1em;
  color: white;
}
#menulo {
  position: absolute;
} */
</style>