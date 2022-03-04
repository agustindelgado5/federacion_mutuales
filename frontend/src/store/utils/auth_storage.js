export function deleteSessionStorage() {
    sessionStorage.removeItem('user')
}

export function hasActiveSessionStorage() {
    return getUser() ? true : false;
}

export function refreshSession() {

}

export function getUser() {
    if (sessionStorage.getItem('user')) {
        return JSON.parse(sessionStorage.getItem('user'))
    } else {
        return false
    }
}

export async function logUser(username, password) {
    try{
        const res = await fetch(process.env.VUE_APP_API_URL + ':' + process.env.VUE_APP_API_PORT + process.env.VUE_APP_API_JWT_CREATE_ENDPOINT,{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
            mode: "cors",
            });
            if(res.statusCode === 200){
                return true
            }
            return false

    }catch (error) {
        console.error(error)
    }
}
