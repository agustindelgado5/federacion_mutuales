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
                <b-button class="accesorapido" style="background-color:darkorange;">Acceso 1</b-button>
                <b-button class="accesorapido" style="background-color:dodgerblue;">Acceso 2</b-button>
                <b-button class="accesorapido" style="background-color:deeppink;">Acceso 3</b-button>
                <b-button class="accesorapido" style="background-color:dodgerblue;">Acceso 4</b-button>
                <b-button class="accesorapido" style="background-color:darkorange;">Acceso 5</b-button>
            </div>
        </b-jumbotron>
    </div>
</template>

<script>
    import VueAwesomplete from "vue-awesomplete";
    import axios from "axios";
    import { APIControler } from "../store/APIControler";
    import VueCookies from 'vue-cookies';

    export default {
        data() {
            return {
                usuario: true
            }
        },
        methods: {
            prueba()
            {
                console.log($cookies.get('usuario'))
            },
            logout()
            {
                axios.post('http://localhost:8081/auth/logout/',
                    {})
                    .then(resp => {
                        swal("Operación Exitosa", " ", "success");
                        $cookies.set('usuario', null);
                        window.location.replace("/login");
                    })
                    .catch(err => {
                        swal("¡ERROR!", "Error en logout", "error");
                        console.log(err)
                    })
            },
            redirect() {
                var user = $cookies.get('usuario');
                if (null == user) {
                    
                }
                console.log(user)
                
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
    }

        .accesorapido:hover, .accesorapido:focus {
            color: black;
            background-color: white !important;
        }

    #accesosrapidos {
        text-align: center;
    }
</style>
