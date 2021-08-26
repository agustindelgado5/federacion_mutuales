<template>
    <div class="MenuPanel">
        <div class="Menu__panel"
            :style="[
                functionalityStyle,
                positionStyle,
                (isTranslating) ? transitionStyle : {}
            ]"
        >
            <div v-if="list.title" @click="handleHeaderClicked" class="Menu__header">
                <span v-show="showHeaderArrow" class="arrow">
                    <LeftArrowIcon />
                </span>
                {{ list.title }}
            </div>
            <input type="text" id="buscadorepico" v-on:keyup="buscarnow()" class="buscador" ref="buscadormenu" placeholder="Buscar Acciones..." />
            <ul class="Menu__list" ref="menuul">
                <li v-for="item in list.children"
                    @click="handleItemClicked(item)"
                    class="Menu__item"
                >
                    <template v-if="item.children.length > 0" :href="item.link">
                        <div class="text">{{ item.title }}</div>
                        <span class="arrow">
                            <RightArrowIcon />
                        </span>
                    </template>
                    <a v-else :href="item.link">
                        <div class="text">{{ item.title }}</div>
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import RightArrowIcon from '../icons/RightArrowIcon.vue';
import LeftArrowIcon from '../icons/LeftArrowIcon.vue';

export default {
    components: {
        RightArrowIcon,
        LeftArrowIcon,
    },
    props: {
        list: {
            type: Object,
            required: true,
        },
        positionStyle: {
            type: Object,
            required: true,
        },
        showHeaderArrow: {
            type: Boolean,
            default: false,
        },
        isTranslating: {
            type: Boolean,
            default: false,
        },
        handleHeaderClicked: {
            type: Function,
            default: () => {},
        },
        handleItemClicked: {
            type: Function,
            default: () => {},
        },
        functionalityStyle: {
            type: Object,
            required: true,
        },
        transitionStyle: {
            type: Object,
            required: true,
        },
    },
    methods:
    {
        async buscarnow() {
            // Declare variables
            var input, filter, ul, li, a, i, txtValue;
            input = this.$refs.buscadormenu;
            filter = input.value.toUpperCase();
            ul = this.$refs.menuul;
            li = ul.getElementsByTagName('li');

            // Loop through all list items, and hide those who don't match the search query
            for (i = 0; i < li.length; i++) {
                a = li[i].getElementsByTagName("div")[0];
                txtValue = a.textContent || a.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    li[i].style.display = "";
                } else {
                    li[i].style.display = "none";
                }
            }
        }
    },
};

</script>

<style lang="scss" scoped>

ul, li {
    padding: 0;
    margin: 0;
}

#buscadorepico {
    background-image: url('../assets/search.png');
    background-size:8%;
    background-position: 10px 12px;
    background-repeat: no-repeat;
    width: 100%;
    font-size: 16px;
    padding: 12px 20px 12px 40px;
    border: 1px solid #ddd;
    margin-bottom: 12px;
    padding-left:3em;
}

.Menu__header {
    display: flex;
    align-items: center;
    padding-left: 35px;
    height: 50px;
    color: #fff;
    font-size: 16px;
    background-color: #232f3e;
    cursor: pointer;

    .arrow {
        padding-top: 2px;
        fill: #fff;
        margin-right: 10px;
        width: 10px;
        height: 100%;
        display: flex;
        align-items: center;
    }
}

.Menu__list {
    list-style: none;
    padding-bottom: 2px;

    .separator {
        border-bottom: 1px solid #d5dbdb;
        padding: 2px 0 0 0;
        margin: 0;
    }
}

.Menu__item {
    color: #4a4a4a;
    padding-left: 35px;
    height: 45px;
    display: flex;
    align-items: center;
    cursor: pointer;

    a {
        color: #4a4a4a;
        width:100%;
        text-decoration: none;
    }

    .arrow {
        padding-top: 2px;
        padding-left: 15px;
        display: flex;
        align-items: center;
        width: 10px;
        height: 100%;
    }
}
.Menu__item:hover
{
    background-color:darkorange;
}
</style>
