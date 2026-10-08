# Hayday Store Shared Library

A TypeScript library containing shared utilities, API clients, and type definitions used across the Hayday Store ecosystem. This package provides a unified interface for GraphQL API interactions and common functionality.

## 📦 What's Included

### 🔗 **GraphQL API Client**
- Pre-configured GraphQL client with typed operations
- Authentication handling and token management
- Error handling and retry logic
- Query and mutation builders

### 📊 **Type Definitions**
- Complete TypeScript types for all API entities
- GraphQL schema-generated types
- Form validation schemas
- Utility types and interfaces

### 🛠️ **Utility Functions**
- Common helper functions
- Data transformation utilities
- Validation helpers
- Error handling utilities

### 🎯 **API Operations**
- Typed GraphQL queries and mutations
- Fragments for data consistency
- Organized by domain (products, orders, users, etc.)

## 🚀 Installation

This package is part of the Hayday Store monorepo and is automatically available to other workspace packages.

```bash
# In the monorepo root
yarn install

# The shared library will be available as @supastore/lib
```

## 🏗️ Package Structure

```
libs/shared/
├── src/
│   ├── api/                    # GraphQL API client and operations
│   │   ├── index.ts           # Main API client export
│   │   ├── errors.ts          # Error handling utilities
│   │   ├── types.ts           # Generated GraphQL types
│   │   ├── fragments/         # GraphQL fragments
│   │   │   ├── analytics.ts   # Analytics data fragments
│   │   │   ├── cart.ts        # Shopping cart fragments
│   │   │   ├── order.ts       # Order data fragments
│   │   │   ├── payment.ts     # Payment fragments
│   │   │   ├── product.ts     # Product data fragments
│   │   │   ├── shipping.ts    # Shipping fragments
│   │   │   ├── store.ts       # Store configuration fragments
│   │   │   └── user.ts        # User data fragments
│   │   ├── mutations/         # GraphQL mutations
│   │   │   ├── auth.ts        # Authentication mutations
│   │   │   ├── cart.ts        # Cart management mutations
│   │   │   ├── marketing.ts   # Marketing mutations
│   │   │   ├── order.ts       # Order mutations
│   │   │   ├── payment.ts     # Payment mutations
│   │   │   ├── product.ts     # Product mutations
│   │   │   ├── shipping.ts    # Shipping mutations
│   │   │   └── store.ts       # Store mutations
│   │   └── queries/           # GraphQL queries
│   │       ├── analytics.ts   # Analytics queries
│   │       ├── cart.ts        # Cart queries
│   │       ├── category.ts    # Category queries
│   │       ├── marketing.ts   # Marketing queries
│   │       ├── order.ts       # Order queries
│   │       ├── payment.ts     # Payment queries
│   │       ├── product.ts     # Product queries
│   │       ├── shipping.ts    # Shipping queries
│   │       ├── store.ts       # Store queries
│   │       └── user.ts        # User queries
│   └── index.ts               # Main library export
├── package.json               # Package configuration
└── tsconfig.json             # TypeScript configuration
```

## 🔧 Usage

### API Client Setup

```typescript
import { 
  signInAdmin, 
  signOutAdmin,
  getProducts,
  createProduct,
  updateProduct
} from '@supastore/lib';

// Authentication
const authResponse = await signInAdmin({
  dataCheckString: telegramDataString,
});

// Product management
const products = await getProducts({
  storeId: 'store-id',
  first: 10,
});

const newProduct = await createProduct({
  storeId: 'store-id',
  name: 'New Product',
  description: 'Product description',
  price: 29.99,
});
```

### Using with Authentication Headers

```typescript
// With authentication token
const headers = { 
  Authorization: `Bearer ${accessToken}` 
};

const orders = await getOrders({
  storeId: 'store-id',
}, headers);

const updatedOrder = await updateOrderStatus({
  orderId: 'order-id',
  status: 'FULFILLED',
}, headers);
```

### Error Handling

```typescript
import { APIError } from '@supastore/lib';

try {
  const result = await createProduct(productData);
} catch (error) {
  if (error instanceof APIError) {
    // Handle specific API errors
    console.error('API Error:', error.message);
    console.error('Error Code:', error.errorCode);
    console.error('Details:', error.details);
  } else {
    // Handle other errors
    console.error('Unexpected error:', error);
  }
}
```

## 📊 Available API Operations

### Authentication

```typescript
// Admin authentication
signInAdmin(params: SignInAdminInput): Promise<AuthResponse>
signOutAdmin(params: SignOutInput): Promise<boolean>

// User authentication  
signInUser(params: SignInUserInput): Promise<AuthResponse>
```

### Product Management

```typescript
// Queries
getProducts(params: GetProductsInput, headers?: Headers): Promise<ProductConnection>
getProduct(params: GetProductInput): Promise<Product>
getCategories(params: GetCategoriesInput): Promise<Category[]>

// Mutations
createProduct(params: CreateProductInput, headers: Headers): Promise<Product>
updateProduct(params: UpdateProductInput, headers: Headers): Promise<Product>
deleteProduct(params: DeleteProductInput, headers: Headers): Promise<boolean>
```

### Order Management

```typescript
// Queries
getOrders(params: GetOrdersInput, headers: Headers): Promise<OrderConnection>
getOrder(params: GetOrderInput): Promise<Order>

// Mutations
createOrder(params: CreateOrderInput, headers: Headers): Promise<Order>
updateOrderStatus(params: UpdateOrderStatusInput, headers: Headers): Promise<Order>
fulfillOrder(params: FulfillOrderInput, headers: Headers): Promise<Order>
```

### Store Management

```typescript
// Queries
getStore(params: GetStoreInput): Promise<Store>
getStores(headers: Headers): Promise<Store[]>

// Mutations
createStore(params: CreateStoreInput, headers: Headers): Promise<Store>
updateStore(params: UpdateStoreInput, headers: Headers): Promise<Store>
updateStoreBotToken(params: UpdateBotTokenInput, headers: Headers): Promise<boolean>
```

### Cart Operations

```typescript
// Queries
getCart(params: GetCartInput): Promise<Cart>

// Mutations
addToCart(params: AddToCartInput, headers: Headers): Promise<CartItem>
updateCartItem(params: UpdateCartItemInput, headers: Headers): Promise<CartItem>
removeFromCart(params: RemoveFromCartInput, headers: Headers): Promise<boolean>
clearCart(params: ClearCartInput, headers: Headers): Promise<boolean>
```

### Payment Processing

```typescript
// Queries
getPaymentMethods(params: GetPaymentMethodsInput): Promise<PaymentMethod[]>
getPayment(params: GetPaymentInput): Promise<Payment>

// Mutations
createPaymentMethod(params: CreatePaymentMethodInput, headers: Headers): Promise<PaymentMethod>
processPayment(params: ProcessPaymentInput, headers: Headers): Promise<Payment>
updatePaymentStatus(params: UpdatePaymentStatusInput, headers: Headers): Promise<Payment>
```

### Analytics

```typescript
// Queries
getAnalytics(params: GetAnalyticsInput, headers: Headers): Promise<AnalyticsData>
getSalesReport(params: GetSalesReportInput, headers: Headers): Promise<SalesReport>
getCustomerAnalytics(params: GetCustomerAnalyticsInput, headers: Headers): Promise<CustomerAnalytics>
```

### Marketing

```typescript
// Queries
getMailingCampaigns(params: GetMailingCampaignsInput, headers: Headers): Promise<MailingCampaign[]>

// Mutations
createMailingCampaign(params: CreateMailingCampaignInput, headers: Headers): Promise<MailingCampaign>
sendMailing(params: SendMailingInput, headers: Headers): Promise<boolean>
```

## 📋 Type Definitions

### Core Types

```typescript
// User types
interface User {
  id: string;
  username: string;
  firstName: string;
  lastName: string;
  email?: string;
  photoUrl?: string;
  role: UserRole;
}

// Store types
interface Store {
  id: string;
  name: string;
  description?: string;
  storeUrl: string;
  timezone: string;
  logo?: StoreLogoEdge;
  bot?: StoreBot;
}

// Product types
interface Product {
  id: string;
  name: string;
  description: string;
  shortDescription?: string;
  price: number;
  state: ProductState;
  images: ProductImageConnection;
  variants: ProductVariantConnection;
  category?: Category;
}

// Order types
interface Order {
  id: string;
  orderNumber: string;
  fulfilmentStatus: FulfilmentStatus;
  totalAmount: number;
  cart: Cart;
  customer: User;
  payment?: Payment;
  shipping?: ShippingDetails;
  createdAt: string;
}
```

### Input Types

```typescript
// Product creation
interface CreateProductInput {
  storeId: string;
  name: string;
  description: string;
  shortDescription?: string;
  price: number;
  categoryId?: string;
  images?: string[];
  variants?: CreateProductVariantInput[];
}

// Order updates
interface UpdateOrderStatusInput {
  orderId: string;
  status: FulfilmentStatus;
}

// Store configuration
interface UpdateStoreInput {
  storeId: string;
  name?: string;
  description?: string;
  timezone?: string;
}
```

## 🛠️ Development

### Building the Library

```bash
# Build TypeScript
yarn build

# Watch for changes during development
yarn build --watch
```

### Type Generation

GraphQL types are automatically generated from the backend schema:

```bash
# Generate types (run from API backend)
python manage.py graphql_schema --out schema.json

# Update shared library types
# (Manual process - copy generated types to src/api/types.ts)
```

### Linting and Code Quality

```bash
# Run ESLint
yarn lint

# Fix linting issues
yarn lint:fix

# Type checking
yarn type-check
```

## 🔄 GraphQL Fragments

Shared fragments ensure consistency across queries:

```typescript
// Product fragments
export const PRODUCT_FRAGMENT = gql`
  fragment ProductFragment on Product {
    id
    name
    description
    shortDescription
    price
    state
    images {
      edges {
        node {
          id
          url
          altText
        }
      }
    }
    variants {
      edges {
        node {
          id
          sku
          price
          stock
          size {
            id
            value
          }
        }
      }
    }
  }
`;
```

## 🔗 Integration Examples

### React Query Integration

```typescript
// In admin-shop or tg-shop
import { useQuery, useMutation } from '@tanstack/react-query';
import { getProducts, createProduct } from '@supastore/lib';

// Query hook
export function useProducts(storeId: string) {
  return useQuery({
    queryKey: ['products', storeId],
    queryFn: () => getProducts({ storeId, first: 20 }),
  });
}

// Mutation hook
export function useCreateProduct() {
  return useMutation({
    mutationFn: createProduct,
    onSuccess: () => {
      // Invalidate products cache
      queryClient.invalidateQueries(['products']);
    },
  });
}
```

### Next.js API Routes

```typescript
// pages/api/products.ts
import { NextApiRequest, NextApiResponse } from 'next';
import { getProducts } from '@supastore/lib';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  try {
    const products = await getProducts({
      storeId: req.query.storeId as string,
    });
    res.json(products);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch products' });
  }
}
```

## 🔒 Security Considerations

### API Key Management

- Never include API keys in the shared library
- Pass authentication headers at call time
- Use environment variables in consuming applications

### Error Handling

```typescript
// Don't expose internal errors to clients
try {
  return await apiCall();
} catch (error) {
  // Log full error for debugging
  console.error('Internal API Error:', error);
  
  // Return sanitized error to client
  throw new APIError('Operation failed', 500);
}
```

## 🧪 Testing

```bash
# Run tests (when available)
yarn test

# Test with consuming applications
cd ../../apps/admin-shop
yarn dev  # Should use latest shared lib changes
```

## 📚 Additional Resources

- [GraphQL Documentation](https://graphql.org/learn/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Monorepo Best Practices](https://monorepo.tools/)

## 🤝 Contributing

### Adding New API Operations

1. **Define GraphQL operation** in appropriate file (queries/ or mutations/)
2. **Add TypeScript types** for inputs and responses
3. **Create API function** that calls the GraphQL endpoint
4. **Export from index.ts** for external use
5. **Update documentation** with usage examples

### Code Style

- Use TypeScript for all code
- Follow existing naming conventions
- Add JSDoc comments for public APIs
- Keep functions focused and single-purpose

---

**Shared utilities powering the Hayday Store ecosystem!** ⚙️

For more information, check the [main Hayday Store documentation](../../README.md).