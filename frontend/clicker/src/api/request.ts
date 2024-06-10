const DEFAULT_URL = "https://409284db5424.ngrok.app/"

// @ts-ignore
const TG = window.Telegram.WebApp

export default async function request(endpoint: string, method: string="GET", date: any) : Promise<any> {
    const request_data: RequestInit = {
        headers: {authorization: TG.initData},
        body: JSON.stringify(data)
    }

    const responce = await fetch(
        '${DEFAULT_URL}/${endpoint}' ,
        request_data

    )
    if (responce.ok) return await responce.json()
        return undefined
    }