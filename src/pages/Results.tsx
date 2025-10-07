import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { AlertTriangle, CheckCircle2, XCircle, FileText, Download, Send } from "lucide-react";
import { useNavigate } from "react-router-dom";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const Results = () => {
  const navigate = useNavigate();
  const fraudScore = 82;

  return (
    <div className="min-h-screen bg-gradient-hero">
      <Navbar />
      
      <div className="container mx-auto px-4 pt-24 pb-20">
        <div className="max-w-5xl mx-auto space-y-6">
          {/* Summary Card */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-fade-in">
            <CardHeader>
              <div className="flex items-start justify-between">
                <div>
                  <CardTitle className="text-2xl mb-2">Analysis Results</CardTitle>
                  <CardDescription>Loan ID: LN2024001234 | Applicant: Rajesh Kumar</CardDescription>
                </div>
                <Badge variant="destructive" className="text-lg px-4 py-2">
                  High Risk
                </Badge>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-6">
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-lg font-semibold">Fraud Probability</span>
                    <span className="text-3xl font-bold text-destructive">{fraudScore}%</span>
                  </div>
                  <Progress value={fraudScore} className="h-3" />
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-4">
                  <Button onClick={() => navigate("/report")} className="bg-gradient-primary">
                    <FileText className="mr-2 h-5 w-5" />
                    View Detailed Report
                  </Button>
                  <Button variant="outline">
                    <Download className="mr-2 h-5 w-5" />
                    Download PDF
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Breakdown Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
              <CardHeader>
                <CardTitle className="text-lg">Document Authenticity</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-muted-foreground">PAN Card</span>
                  <div className="flex items-center gap-2">
                    <AlertTriangle className="h-5 w-5 text-warning" />
                    <Badge variant="outline" className="border-warning text-warning">Suspicious</Badge>
                  </div>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-muted-foreground">Aadhaar Card</span>
                  <div className="flex items-center gap-2">
                    <CheckCircle2 className="h-5 w-5 text-success" />
                    <Badge variant="outline" className="border-success text-success">Verified</Badge>
                  </div>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-muted-foreground">Marksheet</span>
                  <div className="flex items-center gap-2">
                    <XCircle className="h-5 w-5 text-destructive" />
                    <Badge variant="outline" className="border-destructive text-destructive">Tampered</Badge>
                  </div>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-muted-foreground">Income Certificate</span>
                  <div className="flex items-center gap-2">
                    <CheckCircle2 className="h-5 w-5 text-success" />
                    <Badge variant="outline" className="border-success text-success">Verified</Badge>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.1s' }}>
              <CardHeader>
                <CardTitle className="text-lg">Identity Verification</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-muted-foreground">Face Match Score</span>
                  <span className="font-semibold text-warning">67%</span>
                </div>
                <Progress value={67} className="h-2" />
                
                <div className="flex items-center justify-between pt-2">
                  <span className="text-muted-foreground">Biometric Match</span>
                  <div className="flex items-center gap-2">
                    <XCircle className="h-5 w-5 text-destructive" />
                    <span className="font-semibold text-destructive">Failed</span>
                  </div>
                </div>
                
                <div className="flex items-center justify-between">
                  <span className="text-muted-foreground">Address Match</span>
                  <div className="flex items-center gap-2">
                    <CheckCircle2 className="h-5 w-5 text-success" />
                    <span className="font-semibold text-success">Verified</span>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.2s' }}>
              <CardHeader>
                <CardTitle className="text-lg">Duplicate Applications</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 rounded-full bg-destructive/20 flex items-center justify-center">
                      <span className="text-2xl font-bold text-destructive">3</span>
                    </div>
                    <div>
                      <p className="font-semibold text-destructive">Multiple Applications Detected</p>
                      <p className="text-sm text-muted-foreground">Same identity used across 3 institutions</p>
                    </div>
                  </div>
                  <div className="space-y-2 pt-2">
                    <p className="text-sm font-medium">Flagged Applications:</p>
                    <div className="space-y-1 text-sm text-muted-foreground">
                      <p>• LN2024001234 - IIT Delhi</p>
                      <p>• LN2024000987 - NIT Trichy</p>
                      <p>• LN2023009876 - BITS Pilani</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.3s' }}>
              <CardHeader>
                <CardTitle className="text-lg">Behavioral Analysis</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-muted-foreground">Pattern Match Score</span>
                    <span className="text-xl font-bold text-warning">74%</span>
                  </div>
                  <Progress value={74} className="h-2" />
                  
                  <div className="space-y-2 pt-2">
                    <p className="text-sm font-medium">Suspicious Patterns:</p>
                    <div className="space-y-1 text-sm text-muted-foreground">
                      <p>• Rapid succession applications</p>
                      <p>• Inconsistent employment history</p>
                      <p>• Multiple phone numbers</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Action Buttons */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass">
            <CardContent className="pt-6">
              <div className="flex flex-col md:flex-row gap-4">
                <Button className="flex-1 bg-gradient-primary">
                  <Send className="mr-2 h-5 w-5" />
                  Send for Manual Review
                </Button>
                <Button variant="outline" className="flex-1">
                  Flag Application
                </Button>
                <Button variant="outline" className="flex-1" onClick={() => navigate("/upload")}>
                  Analyze Another
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      <Footer />
    </div>
  );
};

export default Results;
