import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Inscription } from 'src/app/models/Inscription';
import { InscriptionService } from 'src/app/services/inscription-services.service';


@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {
  data!: Inscription;
  form!: FormGroup;

  constructor(private inscriptionService: InscriptionService) { }

  ngOnInit(): void {
    // Genero los validadores para cada campo
    this.form = new FormGroup({
      name: new FormControl(null, [
        Validators.required, 
        Validators.minLength(3), 
        Validators.maxLength(25)
      ]),
      last_name: new FormControl(null, [
        Validators.required, 
        Validators.minLength(3), 
        Validators.maxLength(25)
      ]),
      email: new FormControl(null, [
        Validators.required,
        Validators.email
      ]),
      country: new FormControl(null, [
        Validators.required
      ]),
      phone: new FormControl(null, [
        Validators.required,
        Validators.pattern('[- +()0-9]{10,}'),
        Validators.minLength(10)      
      ]),
      job: new FormControl(null, [
        Validators.required, 
        Validators.minLength(3), 
        Validators.maxLength(25)]),
    })
  }

  onSubmit(): void {
    
  if(!this.form.valid){
    window.alert('Los datos ingresados son inválidos o faltan completar campos')
  } else {
    if (confirm('¿Quiere enviar su información?')){      
        // Creo un objeto Inscripcion y seteo los valares al constructor  
        this.data = new Inscription(
          this.form.value['name'], 
          this.form.value['last_name'],
          this.form.value['email'],
          this.form.value['country'],
          this.form.value['phone'],
          this.form.value['job']);
        this.inscriptionService.save(this.data).subscribe(data => { 
          window.alert(data['message'])
          if (data['message'] == 'La inscripción se realizo correctamente'){
            window.location.reload();  
          }
        });
        
    }
  }
  }
}
