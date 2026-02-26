import { ComponentFixture, TestBed } from "@angular/core/testing";
import { CommonModule } from "@angular/common";

import { ProductList } from './product-list';

describe('ProductList', () => {
  let component: ProductList;
  let fixture: ComponentFixture<ProductList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProductList, CommonModule] 
    }).compileComponents();

    fixture = TestBed.createComponent(ProductList);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  it('should have a non-empty products array', () => {
    expect(component.products.length).toBeGreaterThan(0);
  });

  it('each product should have a name, price, and link', () => {
    component.products.forEach(product => {
      expect(product.name).toBeTruthy();
      expect(product.price).toBeGreaterThan(0);
      expect(product.link).toMatch(/^https?:\/\//);
    });
  });

  it('encodeURIComponent function should exist', () => {
    expect(component.encodeURIComponent).toBeDefined();
    const testStr = "Check this out!";
    expect(component.encodeURIComponent(testStr)).toBe(encodeURIComponent(testStr));
  });
});