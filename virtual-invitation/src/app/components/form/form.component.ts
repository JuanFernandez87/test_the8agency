import { Component, OnInit } from '@angular/core';
import { Inscription } from 'src/app/models/Inscription';
import { InscriptionService } from 'src/app/services/inscription-services.service';


@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {
  data!: Inscription;
  name!: string;
  last_name!: string;
  email!: string;
  country!: string;
  phone!: number;
  job!: string;

  constructor(
    private inscriptionService: InscriptionService
  ) { }

  ngOnInit(): void {
  }

  onCreate(): void {
    this.data = new Inscription(this.name, this.last_name,this.email,this.country,this.phone,this.job);
    this.inscriptionService.save(this.data).subscribe();
  }
}
