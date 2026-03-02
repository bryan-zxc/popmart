# Popmart Vinyl Vault

Keep every vinyl figure safe, organized, and easy to find — Popmart Vinyl Vault is a dedicated storage solution for your growing Popmart collection. Catalog each piece by series, size, and shelf location, so you always know exactly where your favorites live and how much room you have left.

## Features

- **Collection catalog** — Log each figure with series name, character, variant, and condition.
- **Wishlist management** — Track which pieces you're still hunting for.
- **Duplicate tracking** — Identify extras available for trade or sale.
- **Series completion** — See at a glance how close you are to completing each series.
- **Collection stats** — View totals, rarity breakdowns, and collection value estimates.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v16 or later)
- npm (included with Node.js)

### Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd popmart-vinyl-vault
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure the application (optional):
   ```bash
   cp .env.example .env
   ```
   Edit `.env` to set any custom configuration such as the database path or port number.

4. Start the application:
   ```bash
   npm start
   ```

The application will be available at `http://localhost:3000` by default.

### Verifying Your Setup

Run the test suite to confirm everything is working:
```bash
npm test
```

## Contributing

We welcome contributions! Please open an issue or submit a pull request if you'd like to help improve the tracker.

## License

This project is open source. See the [LICENSE](LICENSE) file for details.
