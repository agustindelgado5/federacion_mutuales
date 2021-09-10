<template>
    <div class="vue-tempalte">
        <form>
            <h3>Sign In</h3>

            <div class="form-group">
                <label>Email address</label>
                <input type="email" class="form-control form-control-lg" />
            </div>

            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control form-control-lg" />
            </div>

            <button type="submit" class="btn btn-dark btn-lg btn-block">Log In</button>

            <p class="forgot-password text-right mt-2 mb-4">
                <router-link to="/forgot-password">Forgot password ?</router-link>
            </p>

        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {}
        }
    }
</script>

<style>
    #nav{
        display:none;
    }
    .btn{
        color:darkorange;
    }
    .botonmenu {
        display: none;
    }
    .myTable {
        position: absolute;
        left: 0;
        padding: 1.5em;
        margin-top: 4rem;
        overflow: auto;
        transition: 0.5s;
        width: 100%;
        background-color: red;
    }
    * {
        box-sizing: border-box;
    }
    body {
        text-align: center;
        background: darkorange !important;
        min-height: 100vh;
        font-weight: 400;
        align-content: center !important;
        vertical-align: middle !important;
    }
    form {
        background-color: white;
        padding: 3em;
        border-radius: 3em;
        vertical-align: middle !important;
        width: 100%;
        height: 55%;
        margin-left: auto;
        margin-right: auto;
    }
    html,
    .App,
    .vue-tempalte,
    .vertical-center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top:3em;
        width:50%;
    }
    .navbar-light {
        background-color: #ffffff;
        box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
    }

    .vertical-center {
        display: flex;
        text-align: left;
        justify-content: center;
        flex-direction: column;
        color: white;
    }

    .inner-block {
        width: 450px;
        margin: auto;
        background: #ffffff;
        box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
        padding: 40px 55px 45px 55px;
        border-radius: 15px;
        transition: all .3s;
    }

    .vertical-center .form-control:focus {
        border-color: #2554FF;
        box-shadow: none;
    }

    .vertical-center h3 {
        text-align: center;
        margin: 0;
        line-height: 1;
        padding-bottom: 20px;
        color:white;
    }

    label {
        font-weight: 500;
    }

    .forgot-password,
    .forgot-password a {
        text-align: right;
        font-size: 13px;
        padding-top: 10px;
        color: #7a7a7a;
        margin: 0;
    }

    .forgot-password a {
        color: #2554FF;
    }

</style>
