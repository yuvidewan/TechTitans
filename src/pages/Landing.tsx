import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Upload, Brain, FileCheck, Shield, BarChart3, CheckCircle2 } from "lucide-react";
import { useNavigate } from "react-router-dom";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const Landing = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-hero">
      <Navbar />
      
      {/* Hero Section */}
      <section className="container mx-auto px-4 pt-32 pb-20">
        <div className="max-w-4xl mx-auto text-center space-y-6 animate-fade-in">
          <h1 className="text-5xl md:text-6xl font-bold text-foreground leading-tight">
            Empowering Fair Education
            <br />
            <span className="bg-gradient-primary bg-clip-text text-transparent">
              Smarter Loan Fraud Detection
            </span>
          </h1>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Detect fake documents, identity theft, and multiple applications with AI-powered analysis. 
            Protect educational institutions and deserving students.
          </p>
          <div className="flex flex-wrap gap-4 justify-center pt-4">
            <Button 
              onClick={() => navigate("/login")} 
              size="lg"
              className="bg-gradient-primary text-lg px-8 py-6 shadow-glass"
            >
              Get Started
            </Button>
            <Button 
              onClick={() => navigate("/login")} 
              size="lg"
              variant="outline"
              className="text-lg px-8 py-6"
            >
              Admin Login
            </Button>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-20 max-w-4xl mx-auto">
          <Card className="bg-card/50 backdrop-blur-sm border-border shadow-glass animate-scale-in">
            <CardContent className="pt-6 text-center">
              <div className="text-4xl font-bold bg-gradient-primary bg-clip-text text-transparent">98%</div>
              <p className="text-muted-foreground mt-2">Detection Accuracy</p>
            </CardContent>
          </Card>
          <Card className="bg-card/50 backdrop-blur-sm border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.1s' }}>
            <CardContent className="pt-6 text-center">
              <div className="text-4xl font-bold bg-gradient-primary bg-clip-text text-transparent">10k+</div>
              <p className="text-muted-foreground mt-2">Applications Analyzed</p>
            </CardContent>
          </Card>
          <Card className="bg-card/50 backdrop-blur-sm border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.2s' }}>
            <CardContent className="pt-6 text-center">
              <div className="text-4xl font-bold bg-gradient-primary bg-clip-text text-transparent">50+</div>
              <p className="text-muted-foreground mt-2">Institutions Protected</p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* How It Works */}
      <section className="container mx-auto px-4 py-20">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold mb-4">How It Works</h2>
          <p className="text-xl text-muted-foreground">Simple, fast, and reliable fraud detection in 4 steps</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 max-w-6xl mx-auto">
          <Card className="bg-card/50 backdrop-blur-sm border-border shadow-glass text-center hover:scale-105 transition-transform">
            <CardContent className="pt-8 pb-8">
              <div className="w-16 h-16 mx-auto mb-4 bg-gradient-primary rounded-full flex items-center justify-center">
                <Upload className="h-8 w-8 text-primary-foreground" />
              </div>
              <h3 className="font-semibold text-lg mb-2">Upload Documents</h3>
              <p className="text-sm text-muted-foreground">
                Drag & drop applicant documents for analysis
              </p>
            </CardContent>
          </Card>

          <Card className="bg-card/50 backdrop-blur-sm border-border shadow-glass text-center hover:scale-105 transition-transform">
            <CardContent className="pt-8 pb-8">
              <div className="w-16 h-16 mx-auto mb-4 bg-gradient-primary rounded-full flex items-center justify-center">
                <Brain className="h-8 w-8 text-primary-foreground" />
              </div>
              <h3 className="font-semibold text-lg mb-2">AI Analysis</h3>
              <p className="text-sm text-muted-foreground">
                Advanced ML models process and analyze patterns
              </p>
            </CardContent>
          </Card>

          <Card className="bg-card/50 backdrop-blur-sm border-border shadow-glass text-center hover:scale-105 transition-transform">
            <CardContent className="pt-8 pb-8">
              <div className="w-16 h-16 mx-auto mb-4 bg-gradient-primary rounded-full flex items-center justify-center">
                <BarChart3 className="h-8 w-8 text-primary-foreground" />
              </div>
              <h3 className="font-semibold text-lg mb-2">Fraud Score</h3>
              <p className="text-sm text-muted-foreground">
                Get comprehensive fraud risk assessment
              </p>
            </CardContent>
          </Card>

          <Card className="bg-card/50 backdrop-blur-sm border-border shadow-glass text-center hover:scale-105 transition-transform">
            <CardContent className="pt-8 pb-8">
              <div className="w-16 h-16 mx-auto mb-4 bg-gradient-primary rounded-full flex items-center justify-center">
                <FileCheck className="h-8 w-8 text-primary-foreground" />
              </div>
              <h3 className="font-semibold text-lg mb-2">Verification Result</h3>
              <p className="text-sm text-muted-foreground">
                Detailed report with actionable insights
              </p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Features */}
      <section className="container mx-auto px-4 py-20 bg-card/30 backdrop-blur-sm rounded-3xl my-20">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold mb-4">Key Features</h2>
          <p className="text-xl text-muted-foreground">Comprehensive fraud detection capabilities</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
          {[
            { icon: Shield, title: "Document Authentication", desc: "Verify authenticity of PAN, Aadhaar, and educational documents" },
            { icon: CheckCircle2, title: "Identity Verification", desc: "Cross-check applicant identity across multiple databases" },
            { icon: BarChart3, title: "Duplicate Detection", desc: "Identify multiple applications from same individual" },
            { icon: Brain, title: "Pattern Recognition", desc: "ML-powered behavioral analysis for fraud patterns" },
            { icon: FileCheck, title: "Real-time Analysis", desc: "Instant fraud risk assessment and scoring" },
            { icon: Shield, title: "Secure & Compliant", desc: "Bank-grade security with full data compliance" }
          ].map((feature, i) => (
            <Card key={i} className="bg-card/50 backdrop-blur-sm border-border shadow-glass hover:shadow-lg transition-shadow">
              <CardContent className="pt-6 space-y-3">
                <feature.icon className="h-10 w-10 text-primary" />
                <h3 className="font-semibold text-lg">{feature.title}</h3>
                <p className="text-sm text-muted-foreground">{feature.desc}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default Landing;
