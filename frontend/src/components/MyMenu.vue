<template>
    <div>
        <b-jumbotron header="Federación Tucumana de Mutuales">
            <img src="../assets/logo.jpg" alt="Logo Federación" srcset="" id="Logo_fed" style="margin-top:1em;margin-bottom:1em;">

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
    export default {};
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
