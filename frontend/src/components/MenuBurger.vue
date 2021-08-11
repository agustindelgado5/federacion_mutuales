<template>
    <div class="botonmenu">
        <div @click="handleBurgerClicked" class="Menu__burger">
            <MenuIcon />
        </div>
        <span @click="handleBurgerClicked">Menu</span>
    </div>
</template>

<script>
import MenuIcon from '../icons/MenuIcon.vue';

export default {
    components: {
        MenuIcon,
    },
    props: {
        handleBurgerClicked: {
            type: Function,
            required: true,
        },
    },
};
</script>

<style lang="scss" scoped>

    .Menu__burger {
        width: 30px;
        height: 30px;
        cursor: pointer;
        display:inline-block;
    }
    .botonmenu {
        border-color: black;
        border-width: 2px;
        border-style: solid;
        border-radius: 0.3em;
        top: 1em;
        left: 1em;
        padding-top: 0.4em;
        padding-bottom: 0.4em;
        text-align: center;
        background-color: white;
        position: fixed;
        width: 8%;
    }
    .botonmenu:hover,.botonmenu:focus
    {
        background-color:darkorange;
        transition:0.3s linear;
    }
    .botonmenu span
    {
        display:inline-block;
        font-size:1.3em;
        vertical-align:middle;
        margin-left:0.3em;
        cursor: pointer;
    }
</style>
