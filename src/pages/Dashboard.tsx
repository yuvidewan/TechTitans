import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { BarChart3, TrendingUp, AlertTriangle, Shield, FileText, Users } from "lucide-react";
import { useNavigate } from "react-router-dom";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const Dashboard = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-hero">
      <Navbar />
      
      <div className="container mx-auto px-4 pt-24 pb-20">
        <div className="max-w-7xl mx-auto space-y-6">
          {/* Header */}
          <div className="animate-fade-in">
            <h1 className="text-4xl font-bold mb-2">Admin Dashboard</h1>
            <p className="text-muted-foreground">Monitor fraud detection analytics and system performance</p>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium">Total Applications</CardTitle>
                <FileText className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-3xl font-bold">10,234</div>
                <p className="text-xs text-muted-foreground">
                  <span className="text-success">↑ 12%</span> from last month
                </p>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.1s' }}>
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium">Fraud Detected</CardTitle>
                <AlertTriangle className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-3xl font-bold text-destructive">847</div>
                <p className="text-xs text-muted-foreground">
                  8.3% of total applications
                </p>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.2s' }}>
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium">Detection Accuracy</CardTitle>
                <Shield className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-3xl font-bold text-success">98.2%</div>
                <p className="text-xs text-muted-foreground">
                  <span className="text-success">↑ 0.3%</span> improvement
                </p>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.3s' }}>
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium">Active Users</CardTitle>
                <Users className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-3xl font-bold">56</div>
                <p className="text-xs text-muted-foreground">
                  Across 12 institutions
                </p>
              </CardContent>
            </Card>
          </div>

          {/* Charts Row */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
              <CardHeader>
                <CardTitle>Fraud Trend Analysis</CardTitle>
                <CardDescription>Monthly fraud detection over the past 6 months</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="h-64 flex items-center justify-center">
                  <div className="text-center space-y-4">
                    <TrendingUp className="h-16 w-16 text-muted-foreground mx-auto" />
                    <p className="text-muted-foreground">
                      Chart visualization showing fraud trends over time
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.1s' }}>
              <CardHeader>
                <CardTitle>Institution Performance</CardTitle>
                <CardDescription>Fraud cases by institution</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {[
                    { name: "IIT Delhi", cases: 45, total: 523 },
                    { name: "NIT Trichy", cases: 38, total: 412 },
                    { name: "BITS Pilani", cases: 29, total: 387 },
                    { name: "IIM Bangalore", cases: 22, total: 298 },
                  ].map((inst, i) => (
                    <div key={i} className="space-y-2">
                      <div className="flex items-center justify-between text-sm">
                        <span className="font-medium">{inst.name}</span>
                        <span className="text-muted-foreground">{inst.cases} / {inst.total}</span>
                      </div>
                      <div className="h-2 bg-muted rounded-full overflow-hidden">
                        <div 
                          className="h-full bg-gradient-primary"
                          style={{ width: `${(inst.cases / inst.total) * 100}%` }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Recent Applications */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
            <CardHeader>
              <div className="flex items-center justify-between">
                <div>
                  <CardTitle>Recent Applications</CardTitle>
                  <CardDescription>Latest fraud detection results</CardDescription>
                </div>
                <Button variant="outline" onClick={() => navigate("/upload")}>
                  New Analysis
                </Button>
              </div>
            </CardHeader>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Loan ID</TableHead>
                    <TableHead>Applicant</TableHead>
                    <TableHead>Institution</TableHead>
                    <TableHead>Risk Score</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead>Date</TableHead>
                    <TableHead>Action</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {[
                    { id: "LN2024001234", name: "Rajesh Kumar", inst: "IIT Delhi", risk: 82, status: "high", date: "Jan 15" },
                    { id: "LN2024001233", name: "Priya Sharma", inst: "NIT Trichy", risk: 23, status: "low", date: "Jan 15" },
                    { id: "LN2024001232", name: "Amit Patel", inst: "BITS Pilani", risk: 67, status: "medium", date: "Jan 14" },
                    { id: "LN2024001231", name: "Sneha Reddy", inst: "IIM Bangalore", risk: 15, status: "low", date: "Jan 14" },
                    { id: "LN2024001230", name: "Vikram Singh", inst: "IIT Delhi", risk: 91, status: "high", date: "Jan 13" },
                  ].map((app, i) => (
                    <TableRow key={i}>
                      <TableCell className="font-medium">{app.id}</TableCell>
                      <TableCell>{app.name}</TableCell>
                      <TableCell>{app.inst}</TableCell>
                      <TableCell>
                        <div className="flex items-center gap-2">
                          <span className="font-semibold">{app.risk}%</span>
                        </div>
                      </TableCell>
                      <TableCell>
                        <Badge variant={
                          app.status === 'high' ? 'destructive' :
                          app.status === 'medium' ? 'outline' :
                          'outline'
                        } className={
                          app.status === 'low' ? 'border-success text-success' : ''
                        }>
                          {app.status === 'high' ? 'High Risk' : app.status === 'medium' ? 'Medium' : 'Low Risk'}
                        </Badge>
                      </TableCell>
                      <TableCell>{app.date}</TableCell>
                      <TableCell>
                        <Button 
                          variant="ghost" 
                          size="sm"
                          onClick={() => navigate("/results")}
                        >
                          View
                        </Button>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </div>
      </div>

      <Footer />
    </div>
  );
};

export default Dashboard;
