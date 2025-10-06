import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { Download, ArrowLeft, Send } from "lucide-react";
import { useNavigate } from "react-router-dom";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const Report = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-hero">
      <Navbar />
      
      <div className="container mx-auto px-4 pt-24 pb-20">
        <div className="max-w-6xl mx-auto space-y-6">
          {/* Header */}
          <div className="flex items-center justify-between animate-fade-in">
            <div>
              <Button variant="ghost" onClick={() => navigate("/results")} className="mb-4">
                <ArrowLeft className="mr-2 h-4 w-4" />
                Back to Results
              </Button>
              <h1 className="text-4xl font-bold">Detailed Fraud Report</h1>
              <p className="text-muted-foreground mt-2">Comprehensive analysis and fraud indicators</p>
            </div>
            <Button className="bg-gradient-primary">
              <Download className="mr-2 h-5 w-5" />
              Export PDF
            </Button>
          </div>

          {/* Application Info */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
            <CardHeader>
              <CardTitle>Application Information</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div>
                  <p className="text-sm text-muted-foreground">Loan ID</p>
                  <p className="font-semibold">LN2024001234</p>
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Applicant Name</p>
                  <p className="font-semibold">Rajesh Kumar</p>
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Institution</p>
                  <p className="font-semibold">IIT Delhi</p>
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Application Date</p>
                  <p className="font-semibold">Jan 15, 2024</p>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Document Analysis */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
            <CardHeader>
              <CardTitle>Document Analysis Details</CardTitle>
            </CardHeader>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Document Type</TableHead>
                    <TableHead>Document ID</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead>Issues Found</TableHead>
                    <TableHead>Confidence</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  <TableRow>
                    <TableCell className="font-medium">PAN Card</TableCell>
                    <TableCell>ABCDE1234F</TableCell>
                    <TableCell>
                      <Badge variant="outline" className="border-warning text-warning">Suspicious</Badge>
                    </TableCell>
                    <TableCell>Metadata inconsistency</TableCell>
                    <TableCell>67%</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">Aadhaar Card</TableCell>
                    <TableCell>1234 5678 9012</TableCell>
                    <TableCell>
                      <Badge variant="outline" className="border-success text-success">Verified</Badge>
                    </TableCell>
                    <TableCell>None</TableCell>
                    <TableCell>98%</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">12th Marksheet</TableCell>
                    <TableCell>HS/2020/123456</TableCell>
                    <TableCell>
                      <Badge variant="outline" className="border-destructive text-destructive">Tampered</Badge>
                    </TableCell>
                    <TableCell>Digital manipulation detected</TableCell>
                    <TableCell>89%</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">Income Certificate</TableCell>
                    <TableCell>IC/MH/2023/98765</TableCell>
                    <TableCell>
                      <Badge variant="outline" className="border-success text-success">Verified</Badge>
                    </TableCell>
                    <TableCell>None</TableCell>
                    <TableCell>95%</TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </CardContent>
          </Card>

          {/* Timeline */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
            <CardHeader>
              <CardTitle>Suspicious Activity Timeline</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {[
                  { date: "Jan 15, 2024", event: "Application submitted to IIT Delhi", risk: "normal" },
                  { date: "Jan 10, 2024", event: "Same documents used at NIT Trichy", risk: "high" },
                  { date: "Dec 20, 2023", event: "Document modifications detected", risk: "high" },
                  { date: "Dec 15, 2023", event: "Multiple phone number changes", risk: "medium" },
                  { date: "Nov 30, 2023", event: "First application at BITS Pilani", risk: "normal" }
                ].map((item, i) => (
                  <div key={i} className="flex items-start gap-4 pb-4 border-b border-border last:border-0 last:pb-0">
                    <div className={`w-3 h-3 rounded-full mt-1.5 ${
                      item.risk === 'high' ? 'bg-destructive' : 
                      item.risk === 'medium' ? 'bg-warning' : 
                      'bg-success'
                    }`} />
                    <div className="flex-1">
                      <p className="font-medium">{item.event}</p>
                      <p className="text-sm text-muted-foreground">{item.date}</p>
                    </div>
                    <Badge variant={
                      item.risk === 'high' ? 'destructive' :
                      item.risk === 'medium' ? 'outline' :
                      'outline'
                    }>
                      {item.risk === 'high' ? 'High Risk' : item.risk === 'medium' ? 'Medium Risk' : 'Normal'}
                    </Badge>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Similar Profiles */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
            <CardHeader>
              <CardTitle>Similar Fraudulent Profiles</CardTitle>
            </CardHeader>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Case ID</TableHead>
                    <TableHead>Similarity</TableHead>
                    <TableHead>Common Patterns</TableHead>
                    <TableHead>Outcome</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  <TableRow>
                    <TableCell className="font-medium">FR2023-8765</TableCell>
                    <TableCell>89%</TableCell>
                    <TableCell>Document tampering, multiple applications</TableCell>
                    <TableCell>
                      <Badge variant="destructive">Rejected</Badge>
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">FR2023-7654</TableCell>
                    <TableCell>76%</TableCell>
                    <TableCell>Identity mismatch, rapid applications</TableCell>
                    <TableCell>
                      <Badge variant="destructive">Rejected</Badge>
                    </TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell className="font-medium">FR2024-0123</TableCell>
                    <TableCell>71%</TableCell>
                    <TableCell>Similar document patterns</TableCell>
                    <TableCell>
                      <Badge variant="outline">Under Investigation</Badge>
                    </TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </CardContent>
          </Card>

          {/* Actions */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass">
            <CardContent className="pt-6">
              <div className="flex flex-col md:flex-row gap-4">
                <Button className="flex-1 bg-gradient-primary">
                  <Send className="mr-2 h-5 w-5" />
                  Forward to Investigation Team
                </Button>
                <Button variant="outline" className="flex-1">
                  Add to Watchlist
                </Button>
                <Button variant="outline" className="flex-1">
                  Share Report
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

export default Report;
