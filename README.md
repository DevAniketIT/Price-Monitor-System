# 📊 Professional Price Monitoring System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive, production-ready price monitoring system that tracks product prices across multiple e-commerce platforms with automated alerts, historical analysis, and beautiful visualizations.

## 🌟 Features

### Core Functionality
- **🛒 Multi-Platform Support**: Amazon, Flipkart, and generic e-commerce sites
- **📊 Real-Time Monitoring**: Automated price checking with smart scheduling  
- **🎯 Target Price Alerts**: Get notified when products reach your desired price
- **📈 Historical Analysis**: Track price trends over time with detailed charts
- **💾 Database Storage**: SQLite for local use, PostgreSQL for production

### Advanced Features
- **🔄 Smart Scraping**: User agent rotation and anti-detection mechanisms
- **📧 Email Notifications**: Professional email alerts for price changes
- **📱 REST API**: FastAPI-powered API for integration with other applications
- **📊 Data Visualization**: Beautiful charts with matplotlib and seaborn
- **📋 Export Options**: CSV and Excel reports for external analysis

### Professional Grade
- **⚡ Performance Optimized**: Efficient database queries and caching
- **🛡️ Error Handling**: Comprehensive logging and graceful failure recovery
- **🔧 Highly Configurable**: Customizable scraping rules and alert conditions
- **📈 Scalable Architecture**: Handle thousands of products efficiently

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DevAniketIT/Price-Monitor-System.git
   cd price-monitor-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the demo**:
   ```bash
   python price_monitor_system.py
   ```

### Basic Usage

```python
from price_monitor_system import PriceMonitor

# Initialize the monitor
monitor = PriceMonitor()

# Add a product to monitor
product_id = monitor.add_product(
    name="iPhone 15 Pro",
    url="https://amazon.com/dp/B0CHX9CY7W",
    target_price=999.00
)

# Check prices manually
monitor.check_single_product(product_id)

# Or check all products
monitor.check_all_products()

# Generate reports
report = monitor.get_summary_report()
chart_file = monitor.generate_price_chart(product_id)
```

## 📖 Documentation

### System Architecture

The system consists of several key components:

1. **PriceMonitor**: Core monitoring class with scraping logic
2. **Database Layer**: SQLite/PostgreSQL for data persistence
3. **EmailNotifier**: Automated email alert system
4. **API Layer**: FastAPI REST endpoints for external integration
5. **Visualization**: Chart generation and data export utilities

### Supported E-commerce Platforms

| Platform | Status | Features |
|----------|--------|----------|
| Amazon | ✅ Full Support | Price, availability, product name |
| Flipkart | ✅ Full Support | Price, availability, product name |
| Generic Sites | ✅ Basic Support | Pattern-based price extraction |

### Database Schema

#### Products Table
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    target_price REAL,
    current_price REAL,
    last_checked TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT 1
);
```

#### Price History Table
```sql
CREATE TABLE price_history (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    price REAL NOT NULL,
    availability BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products (id)
);
```

## 🔧 API Usage

Start the FastAPI server:
```bash
python price_monitor_api.py
```

### Key Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/products` | List all monitored products |
| `POST` | `/products` | Add new product to monitor |
| `GET` | `/products/{id}` | Get specific product details |
| `PUT` | `/products/{id}` | Update product settings |
| `DELETE` | `/products/{id}` | Remove product from monitoring |
| `POST` | `/check-prices` | Trigger price check |
| `GET` | `/products/{id}/history` | Get price history |
| `GET` | `/alerts` | Get recent alerts |

### Example API Usage

```python
import requests

# Add a product via API
response = requests.post("http://localhost:8000/products", json={
    "name": "MacBook Pro 16\"",
    "url": "https://amazon.com/dp/B09JQKBQSB",
    "target_price": 2299.00
})

product = response.json()

# Get price history
history = requests.get(f"http://localhost:8000/products/{product['id']}/history")
```

## 📊 Data Export & Visualization

### Generate Reports
```python
# Excel report with multiple sheets
excel_file = monitor.generate_excel_report()

# CSV export
csv_files = monitor.export_to_csv(export_type="all")

# Price charts
chart_file = monitor.generate_price_chart(product_id, days=30)
```

### Sample Visualizations

The system generates professional charts showing:
- Price trends over time
- Minimum, maximum, and current prices
- Target price indicators
- Availability status

## 🔔 Email Notifications

Set up email alerts for price changes:

```python
from price_monitor_system import EmailNotifier

# Configure email
notifier = EmailNotifier()
notifier.setup_email(
    email="your-email@gmail.com",
    password="your-app-password",  # Use Gmail App Password
    recipients=["alert@yourdomain.com"]
)

# Automatic alerts are sent when:
# - Price drops by 5% or more
# - Target price is reached
# - Product comes back in stock
```

## ⚙️ Configuration

### Environment Variables
```bash
# Optional: PostgreSQL connection
DATABASE_URL=postgresql://user:password@localhost/pricedb

# Email configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Customization Options

1. **Scraping Intervals**: Modify `setup_scheduler()` function
2. **Alert Thresholds**: Adjust percentage triggers in `check_single_product()`
3. **User Agent Rotation**: Add more user agents in `__init__()`
4. **Site Support**: Extend scraping methods for new e-commerce sites

## 📈 Performance & Scalability

### Optimization Features
- **Connection Pooling**: Reuse HTTP connections for better performance
- **Rate Limiting**: Respectful delays to avoid being blocked
- **Database Indexing**: Optimized queries for large datasets
- **Async Support**: FastAPI endpoints for concurrent operations

### Recommended Limits
- **SQLite**: Up to 1,000 products for personal use
- **PostgreSQL**: Unlimited products for enterprise use
- **Scraping Frequency**: Maximum once per hour per product
- **Concurrent Checks**: 5-10 products simultaneously

## 💼 Business Applications

### Freelance Opportunities
- **Custom Price Monitoring**: $200-500 per project
- **E-commerce Integration**: $500-1000 per implementation  
- **Data Analysis Services**: $30-80 per hour
- **Recurring Monitoring**: $50-150 monthly per client

### Enterprise Features
- White-label solutions for retailers
- API integration for inventory management
- Custom alert systems for procurement teams
- Competitive pricing intelligence

## 🧪 Testing

Run the test suite:
```bash
# Basic functionality test
python -m pytest tests/

# Run demo with sample data
python price_monitor_system.py
```

### Test Coverage
- ✅ Database operations
- ✅ Web scraping functionality  
- ✅ Price change detection
- ✅ Alert generation
- ✅ API endpoints
- ✅ Export functionality

## 🔐 Security & Ethics

### Responsible Scraping
- Respectful request rates (2-5 second delays)
- User agent rotation to minimize server load
- Error handling to avoid infinite retry loops
- Compliance with robots.txt when applicable

### Data Privacy
- Local database storage by default
- No data collection or external transmission
- Secure email credential handling
- Optional encryption for sensitive data

## 🚀 Deployment Options

### Local Development
```bash
python price_monitor_system.py
```

### Production Deployment
```bash
# Using Gunicorn for API
gunicorn price_monitor_api:app -w 4 -k uvicorn.workers.UvicornWorker

# With Docker
docker build -t price-monitor .
docker run -p 8000:8000 price-monitor
```

### Cloud Deployment
- **Heroku**: Deploy with PostgreSQL addon
- **DigitalOcean**: Use App Platform for easy scaling
- **AWS**: Lambda functions for serverless monitoring
- **Railway**: Simple deployment with managed databases

## 📋 Project Structure

```
price-monitor-system/
├── price_monitor_system.py    # Core monitoring system
├── price_monitor_api.py       # FastAPI REST API
├── requirements.txt           # Python dependencies
├── README.md                 # This documentation
├── tests/                    # Test files
├── examples/                 # Usage examples
├── docs/                     # Additional documentation
└── scripts/                  # Utility scripts
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for API changes
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **BeautifulSoup**: For HTML parsing capabilities
- **Requests**: For reliable HTTP requests
- **FastAPI**: For modern API development
- **Matplotlib**: For beautiful data visualizations
- **SQLite/PostgreSQL**: For robust data storage

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/DevAniketIT/Price-Monitor-System/issues)
- **Discussions**: [GitHub Discussions](https://github.com/DevAniketIT/Price-Monitor-System/discussions)
- **Email**: DevAniketIT@example.com

## 🎯 Roadmap

### Version 2.0 Planned Features
- [ ] Machine learning price prediction
- [ ] Mobile app companion
- [ ] Webhook integrations
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Cryptocurrency price tracking

---

**Built with ❤️ for the Python community**

*This project demonstrates professional Python development practices and is perfect for portfolio showcasing, freelance projects, or enterprise applications.*
