export class Inscription {
    id!:number;
    name: string;
    last_name: string;
    email: string;
    country: string;
    phone: number;
    job: string;

    constructor(name:string, last_name:string, email:string, country:string, phone:number, job:string) {
        this.name = name;
        this.last_name = last_name;
        this.email = email;
        this.country = country;
        this.phone = phone;
        this.job = job;
    }
}