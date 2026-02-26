export interface Product {
    id: number;
    name: string;
    description: string;
    price: number;
    rating: number;            // 1–5 (can be decimal)
    images: string[];          // gallery images (min 3)
    link: string;  
}