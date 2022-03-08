<template >
    <div>

        <!--HEAD DE LA PAGINA -->
        <vue-headful title="Home - Federación Tucumana de Mutuales"></vue-headful>
        <b-jumbotron header="Federación Tucumana de Mutuales">
            <img src="../assets/logo.jpg" alt="Logo Federación" srcset="" id="Logo_fed" style="margin-top:1em;margin-bottom:1em;">
            <form @submit.prevent="logout" v-if="logout" style="text-align:center;">
                <b-button class="accesorapido" type="submit" style="background-color:red;align-content:center;">Logout</b-button>
            </form>
            <!--<form @submit.prevent="prueba" style="text-align:center;">
        <b-button class="accesorapido" type="submit" style="background-color:red;align-content:center;">probar</b-button>
    </form>-->
            <p style="text-align:center;font-size:1.7em;">Accesos Rápidos</p>
            <div id="accesosrapidos">
                <b-button class="accesorapido" href="/socios/" style="background-color:darkorange;">Agregar Socio</b-button>
                <b-button class="accesorapido" href="/cuotas/" style="background-color:dodgerblue;">Cuota Socio</b-button>
                <b-button class="accesorapido" href="/estudios/" style="background-color:deeppink;">Autorizar Estudio</b-button>
                <b-button class="accesorapido" href="/ordenes/" style="background-color:dodgerblue;">Orden de Consulta</b-button>
                <b-button class="accesorapido" href="/pagadoprofesionales/" style="background-color:darkorange;">Pago a Profesional</b-button>
            </div>
        </b-jumbotron>
    </div>
</template>

<script>
    import VueAwesomplete from "vue-awesomplete";
    import axios from "axios";
    import { Fetcher } from "@/store/utils/Fetcher";
    import { APIControler } from "../store/APIControler";
    import VueCookies from 'vue-cookies';

    export default {
        data() {
            return {
                usuario: true,
                fetcher: new Fetcher(),
            }
        },
        methods: {
            prueba()
            {
                console.log($cookies.get('usuario'))
            },
            logout()
            {
                this.fetcher.logout()
                location.reload()
            },
            redirect() {
                var user = $cookies.get('usuario');
                if (null == user) {

                }
            },
        },
        computed:
        {
            controlarusuario: function () {
                if ($cookies.get('usuario') != null) {
                    this.usuario = true
                } else {
                    this.usuario = false
                }
            }

        },
        beforeMount() {
            this.redirect();
        },

    };
</script>

<style>
    h1 {
        text-align: center;
    }

    #Logo_fed {
        width: 25%;
        display: block;
        margin: auto;
    }

    .accesorapido {
        margin: 1em;
        text-align: center;
        align-content: center;
        color: white !important;
    }

        .accesorapido:hover, .accesorapido:focus {
            color: black !important;
            background-color: white !important;
        }

    #accesosrapidos {
        text-align: center;
        color: white;
    }
</style>
