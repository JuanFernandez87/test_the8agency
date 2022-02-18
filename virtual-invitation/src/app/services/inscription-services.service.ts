import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Inscription } from '../models/Inscription';

@Injectable({
  providedIn: 'root'
})
export class InscriptionService {

  URL = "http://127.0.0.1:8000/api/";

  constructor(private httpClient: HttpClient) { }

  public save(inscription: Inscription): Observable<any> {
    console.log('Contenido inspription', inscription)
    return this.httpClient.post<Inscription>(this.URL + 'invitees/', inscription);
  }
}