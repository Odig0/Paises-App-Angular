import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';


@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styles: [
    `
     li{
        cursor: pointer;
     }
    `
  ]
})
export class SidebarComponent {

}
