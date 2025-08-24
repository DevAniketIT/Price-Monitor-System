#!/usr/bin/env python3
"""
Price Monitor System - Example Usage
Demonstrates how to use the price monitoring system for various scenarios
"""

from price_monitor_system import PriceMonitor, EmailNotifier
import time

def basic_example():
    """Basic usage example"""
    print("🚀 Basic Price Monitoring Example")
    print("=" * 50)
    
    # Initialize the monitor
    monitor = PriceMonitor("example_prices.db")
    
    # Example products to monitor (you can replace with real URLs)
    products = [
        {
            "name": "iPhone 15 Pro",
            "url": "https://www.amazon.com/Apple-iPhone-15-Pro-256GB/dp/B0CHX9CY7W",
            "target_price": 999.00
        },
        {
            "name": "MacBook Pro 16\"",
            "url": "https://www.amazon.com/Apple-MacBook-16-inch-10-core-16-core/dp/B09JQKBQSB",
            "target_price": 2299.00
        },
        {
            "name": "Sony WH-1000XM4",
            "url": "https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863TXGM3",
            "target_price": 250.00
        }
    ]
    
    # Add products to monitor
    product_ids = []
    for product in products:
        print(f"Adding product: {product['name']}")
        product_id = monitor.add_product(
            product['name'], 
            product['url'], 
            product['target_price']
        )
        if product_id:
            product_ids.append(product_id)
        time.sleep(1)  # Be respectful to servers
    
    print(f"\n✅ Added {len(product_ids)} products to monitor")
    return monitor, product_ids

def api_example():
    """Example using the REST API"""
    print("\n📡 API Usage Example")
    print("=" * 50)
    
    try:
        import requests
        
        # Test if API is running
        try:
            response = requests.get("http://localhost:8000/", timeout=5)
            if response.status_code == 200:
                print("✅ API is running!")
                
                # Add a product via API
                new_product = {
                    "name": "Gaming Laptop Example",
                    "url": "https://example.com/gaming-laptop",
                    "target_price": 1299.00
                }
                
                response = requests.post(
                    "http://localhost:8000/products", 
                    json=new_product
                )
                
                if response.status_code == 201:
                    product = response.json()
                    print(f"✅ Added product via API: {product['name']}")
                    
                    # Get all products
                    response = requests.get("http://localhost:8000/products")
                    products = response.json()
                    print(f"📦 Total products via API: {len(products)}")
                else:
                    print(f"❌ Failed to add product: {response.status_code}")
            else:
                print("❌ API not responding correctly")
                
        except requests.exceptions.RequestException:
            print("⚠️ API not running. Start with: python price_monitor_api.py")
            
    except ImportError:
        print("⚠️ 'requests' not installed. Install with: pip install requests")

def email_alerts_example():
    """Example of setting up email alerts"""
    print("\n📧 Email Alerts Setup Example")
    print("=" * 50)
    
    # This is just a demo - don't put real credentials in code!
    print("📝 To set up email alerts:")
    print("1. Get a Gmail App Password from your Google Account")
    print("2. Use the following code structure:")
    
    example_code = '''
    from price_monitor_system import EmailNotifier
    
    # Initialize email notifier
    notifier = EmailNotifier()
    
    # Setup with your credentials
    notifier.setup_email(
        email="your-email@gmail.com",
        password="your-app-password",  # Gmail App Password
        recipients=["alerts@yourdomain.com", "backup@yourdomain.com"]
    )
    
    # Send test alert
    notifier.send_alert(
        subject="Price Alert Test",
        message="This is a test alert from the Price Monitor System!"
    )
    '''
    
    print(example_code)
    print("🔒 Security Note: Never commit real credentials to version control!")

def data_analysis_example(monitor, product_ids):
    """Example of data analysis and reporting"""
    print("\n📊 Data Analysis Example")
    print("=" * 50)
    
    if not product_ids:
        print("⚠️ No products to analyze")
        return
    
    # Generate summary report
    report = monitor.get_summary_report()
    print(f"📈 Summary Report:")
    print(f"   • Total Products: {report['summary']['total_products']}")
    print(f"   • Recent Alerts: {report['summary']['total_alerts']}")
    print(f"   • Average Price: ${report['summary']['avg_current_price']:.2f}")
    
    # Show product details
    if not report['products'].empty:
        print(f"\n📦 Product Details:")
        for _, product in report['products'].iterrows():
            print(f"   • {product['name']}")
            if product['current_price']:
                print(f"     Current: ${product['current_price']:.2f}")
            if product['target_price']:
                print(f"     Target: ${product['target_price']:.2f}")
            if product['lowest_price'] and product['highest_price']:
                print(f"     Range: ${product['lowest_price']:.2f} - ${product['highest_price']:.2f}")
    
    # Generate charts for first product
    if product_ids:
        print(f"\n📊 Generating price chart for first product...")
        chart_file = monitor.generate_price_chart(product_ids[0])
        if chart_file:
            print(f"✅ Chart saved: {chart_file}")
    
    # Export data
    print(f"\n💾 Exporting data...")
    csv_files = monitor.export_to_csv(export_type="products")
    if csv_files:
        print(f"✅ CSV exported: {csv_files}")
    
    excel_file = monitor.generate_excel_report()
    if excel_file:
        print(f"✅ Excel report: {excel_file}")

def production_tips():
    """Tips for production deployment"""
    print("\n🚀 Production Deployment Tips")
    print("=" * 50)
    
    tips = [
        "1. Set up PostgreSQL for better performance and scalability",
        "2. Use environment variables for sensitive configuration",
        "3. Implement proper rate limiting (1-5 second delays between requests)",
        "4. Set up monitoring and alerting for system health",
        "5. Use a task scheduler (cron/systemd) for automated checks",
        "6. Implement proper logging and error handling",
        "7. Consider using Redis for caching frequently accessed data",
        "8. Set up backup strategies for your database",
        "9. Use HTTPS for API endpoints in production",
        "10. Monitor disk usage as database grows over time"
    ]
    
    for tip in tips:
        print(f"   {tip}")
    
    print(f"\n💰 Business Applications:")
    print(f"   • Freelance projects: $200-500 per custom implementation")
    print(f"   • Recurring monitoring services: $50-150/month per client")
    print(f"   • Enterprise solutions: $1000-5000 for comprehensive systems")
    print(f"   • Data analysis services: $30-80/hour")

def main():
    """Main example runner"""
    print("🎯 Price Monitor System - Complete Examples")
    print("=" * 60)
    
    # Basic example
    monitor, product_ids = basic_example()
    
    # API example
    api_example()
    
    # Email alerts example
    email_alerts_example()
    
    # Data analysis example
    data_analysis_example(monitor, product_ids)
    
    # Production tips
    production_tips()
    
    print(f"\n✅ Examples completed!")
    print(f"🔍 Check the generated files:")
    print(f"   • example_prices.db - SQLite database")
    print(f"   • price_chart_*.png - Price history charts")
    print(f"   • *.csv - Exported data files")
    print(f"   • *.xlsx - Excel reports")
    
    print(f"\n📚 Next Steps:")
    print(f"   1. Customize the product URLs with real e-commerce links")
    print(f"   2. Set up email alerts with your Gmail credentials")
    print(f"   3. Deploy the API with: python price_monitor_api.py")
    print(f"   4. Set up automated scheduling for regular price checks")
    print(f"   5. Create a GitHub repository and start building your portfolio!")

if __name__ == "__main__":
    main()
