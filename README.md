# Vinyl Vault

Your personal vinyl record collection, organized and always at your fingertips. Vinyl Vault helps collectors catalog every LP, EP, and single they own — tracking artist, album, pressing details, and condition so nothing gets lost in the stacks.

## Features

- **Record catalog** — Log each record with artist, album title, label, release year, format, and condition.
- **Wishlist** — Keep a running list of records you're hunting for at shops and online.
- **Duplicate detection** — Spot duplicate pressings so you know what's available for trade or sale.
- **Collection stats** — View totals by genre, decade, format, and estimated collection value.
- **Discography tracking** — See how close you are to completing an artist's full discography.

## Tech Stack

- **Node.js** — Server-side runtime
- **Python** — Data processing and scripting
- **PostgreSQL** — Primary relational database
- **Redis** — Caching and session management

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v16 or later)
- npm (included with Node.js)

### Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd vinyl-vault
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure the application (optional):
   ```bash
   cp .env.example .env
   ```
   Edit `.env` to set any custom configuration such as the database connection string or server port.

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

Contributions are welcome! Please open an issue or submit a pull request if you'd like to help improve Vinyl Vault.

## License

This project is open source. See the [LICENSE](LICENSE) file for details.
