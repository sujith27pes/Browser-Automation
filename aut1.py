import pyautogui
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.bing.com/")  # Replace with your desired search engine
search_terms= ['Analysis', 'Business Plan', 'Consultation', 'Data Integration', 'Enterprise Solution', 'Financial Report', 'Global Strategy', 'Human Resources', 'Infrastructure Optimization', 'Job Evaluation', 'Key Performance Indicator', 'Logistics Management', 'Market Research', 'Networking Protocol', 'Operational Efficiency', 'Performance Metrics', 'Quality Assurance', 'Risk Mitigation', 'Strategic Alignment', 'Team Collaboration', 'User Experience', 'Vendor Management', 'Workflow Automation', 'Xenon Lighting Solutions', 'Yearly Forecast', 'Zero-based Budgeting', 'Agile Methodology', 'Brand Development', 'Customer Relationship Management', 'Digital Transformation', 'E-commerce Platform', 'Facility Management', 'Global Expansion', 'Holistic Approach', 'Information Security', 'Joint Venture', 'Knowledge Transfer', 'Leadership Development', 'Mobile App Development', 'Network Security', 'Organizational Culture', 'Project Management', 'Quantitative Analysis', 'Revenue Growth', 'Supply Chain Optimization', 'Technology Integration', 'Unified Communication', 'Value Proposition', 'Webinar Hosting', 'Xponential Growth Strategy', 'Year-end Review', 'Zero Downtime']
 
for term in search_terms:
    # Find search input field
    search_box = driver.find_element("name", "q")

    # Enter search term
    search_box.send_keys(term)

    # Submit search
    search_box.submit()

    # Pause for page loading and viewing
    time.sleep(10)  # Adjust the delay as needed

    # Navigate back to search page for the next search
    driver.back()
driver.quit()

