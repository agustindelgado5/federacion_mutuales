export class Fetcher {
    constructor(
        url = process.env.VUE_APP_API_URL,
        port = process.env.VUE_APP_API_PORT,
    ) {
        this.wrapperURL = new URL(url);
        this.wrapperURL.port = port;
        // this.accessToken = loadSessionStorage().access
    }

    setPathname(pathname) {
        this.wrapperURL.pathname = pathname;
    }

    addParams(key, value) {
        this.wrapperURL.searchParams.append(key, value);
    }

    deleteParams(key) {
        this.wrapperURL.searchParams.delete(key)
    }

    async fetch() {
        // try {
        //     let response = await fetch(this.wrapperURL, {
        //         method: 'GET',
        //         headers: { "Authorization": "Bearer " + this.accessToken }
        //     });
        //     if (response.status === 401) {
        //         let responseRefresh = await refreshSession()
        //         if (responseRefresh.status !== 200) {
        //             deleteSessionStorage()
        //         } else {
        //             this.accessToken = responseRefresh.json().access
        //             console.log(this.accessToken)
        //             let userTemp = loadSessionStorage()
        //             userTemp.access = this.accessToken
        //             sessionStorage.setItem("user", JSON.stringify(userTemp))
        //         }
        //         // refresh token
        //         // si no refresh
        //         // deslogear usuario
        //     }
        //     return response;
        // } catch (error) {
        //     console.error(error);
        // }
    }
}