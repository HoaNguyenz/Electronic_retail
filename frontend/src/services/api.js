import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000'

// Products APIs
export const fetch_categories = async ()=>{
    try {
        const response = await axios.get(`${API_BASE_URL}/products/categories`);
        console.log(response.data);
        return response.data;
    } catch (error){
        console.error('Error fetching categories:', error);
        throw error;
    }
}

export const fetch_marketing_imgaes = async () =>{
    try {
        const response = await axios.get(`${API_BASE_URL}/products/marketing`);
        console.log(response.data);
        return response.data;
    }
    catch (error){
        console.error('Error fetching orders:', error);
        throw error;
    }
}

export const fetch_products = async (filters = {}) => {
    try {
        // Build query string from filters
        const params = new URLSearchParams();
        if (filters.category_id) params.append('category_id', filters.category_id);
        if (filters.category_name) params.append('category_name', filters.category_name);
        if (filters.min_price) params.append('min_price', filters.min_price);
        if (filters.max_price) params.append('max_price', filters.max_price);
        if (filters.brand) params.append('brand', filters.brand);
        if (filters.rating) params.append('rating', filters.rating);

        const url = `${API_BASE_URL}/products${params.toString() ? '?' + params.toString() : ''}`;
        const response = await axios.get(url);
        // Expecting { products: [...] }
        return response.data.products;
    } catch (error) {
        console.error('Error fetching products:', error);
        throw error;
    }
};

export const get_product_detail = async (product_id) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/product`, {
            params: { product_id }
        });
        // Expecting { product: { ... } }
        return response.data.product;
    } catch (error) {
        console.error('Error fetching product detail:', error);
        throw error;
    }
};

// Order APIS
export const fetch_orders = async (user_id) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/order/history?customer_id=${user_id}`);
        console.log(response.data);
        return response.data;
    }
    catch (error){
        console.error('Error fetching orders:', error);
        throw error;
    }
}

// Shopping cart APIs
export const add_to_cart = async ({ customer_id, order_id, product_id, quantity }) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/shoppingcart/add`, {
            customer_id,
            order_id,
            product_id,
            quantity
        });
        return response.data;
    } catch (error) {
        console.error('Error adding to cart:', error);
        throw error;
    }
};

export const remove_item_cart = async (order_item_id) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/shoppingcart/remove`, {
            order_item_id
        });
        // Expecting a success message or updated cart
        return response.data;
    } catch (error) {
        console.error('Error removing item from cart:', error);
        throw error;
    }
};
export const get_cart_count = async ({ customer_id }) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/shoppingcart/count`, {
            params: { customer_id }
        });
        // Expecting { count: ... }
        return typeof response.data.count === "number" ? response.data.count : null;
    } catch (error) {
        console.error('Error fetching cart count:', error);
        return null;
    }
};

export const get_cart_items = async ({ customer_id }) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/shoppingcart/checkout`, {
            params: { customer_id }
        });
        // Expecting { orders: [...], status: 200 }
        return response.data.orders;
    } catch (error) {
        console.error('Error fetching cart items:', error);
        return [];
    }
};

// Payment APIs

export const make_payment = async ({ customer_id, order_id, payment_method }) => {
    try {
        console.log( customer_id, order_id, payment_method)
        const response = await axios.post(`${API_BASE_URL}/payment`, {
            customer_id,
            order_id,
            payment_method
        });
        // Expecting a payment confirmation or status
        return response.data;
    } catch (error) {
        console.error('Error making payment:', error);
        throw error;
    }
};


// Admin APIs

export const admin_add_product = async ({ name, description, price, category_id, supplier_id, warranty_period }) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/admin/add_product`, {
            name,
            description,
            price,
            category_id,
            supplier_id,
            warranty_period
        });
        return response.data;
    } catch (error) {
        console.error('Error adding product:', error);
        throw error;
    }
};

export const admin_update_product = async ({ product_id, name, description, price, category_id, supplier_id, warranty_period }) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/admin/update_product`, {
            product_id,
            name,
            description,
            price,
            category_id,
            supplier_id,
            warranty_period
        });
        return response.data;
    } catch (error) {
        console.error('Error updating product:', error);
        throw error;
    }
};

export const admin_remove_product = async ({ product_id }) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/admin/remove_product`, {
            product_id
        });
        return response.data;
    } catch (error) {
        console.error('Error removing product:', error);
        throw error;
    }
};
// ...existing code...