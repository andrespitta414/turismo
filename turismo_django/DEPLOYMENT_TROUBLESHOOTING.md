# AWS Deployment Troubleshooting Guide

## Current Issue: Free Tier Instance Type Problem

### Problem Identified:
- Error: "The specified instance type is not eligible for Free Tier"
- Current instance: `t2.micro` not eligible in us-east-1
- Environment status: "Launching" but failing

### Solutions to Try:

## Option 1: Use Different Instance Type
```powershell
# Try t3.nano (smaller, more likely to be free tier eligible)
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" create turismo-production-v3 --instance-type t3.nano --region us-east-1
```

## Option 2: Change Region
Some regions have different Free Tier availability:
```powershell
# Try us-west-2 (Oregon)
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" create turismo-production-west --instance-type t2.micro --region us-west-2
```

## Option 3: Use AWS Console
1. Go to AWS Elastic Beanstalk Console
2. Create environment manually
3. Select "Python" platform
4. Choose "t2.micro" or "t3.nano" instance
5. Check "Free Tier eligible" box

## Option 4: Alternative Free Hosting
If AWS continues to fail:

### Heroku (Free Tier)
```bash
# Install Heroku CLI
npm install -g heroku

# Login
heroku login

# Create app
heroku create turismo-django

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### PythonAnywhere (Free Tier)
- Upload project to PythonAnywhere
- Configure web app
- Free tier available

### Vercel (Free for Django)
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

## Current Status:
- Application: `turismo_django` created
- Environment: `turismo-production` (stuck in Launching)
- Region: `us-east-1`
- Issue: Instance type not Free Tier eligible

## Next Steps:
1. Try different instance type
2. Try different region
3. Use AWS Console for manual setup
4. Consider alternative hosting if AWS continues to fail

## Files Created:
- `.ebextensions/01_python.config` - Python configuration
- `.ebextensions/02_instance.config` - Instance configuration
- `requirements.txt` - Dependencies
- `wsgi.py` - WSGI configuration

## Commands to Monitor:
```powershell
# Check status
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" status

# View events
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" events

# Terminate stuck environment (if needed)
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" terminate turismo-production
```
