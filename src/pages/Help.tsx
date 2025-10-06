import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { BookOpen, MessageCircle, AlertCircle, Shield, FileText, HelpCircle } from "lucide-react";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import { useToast } from "@/hooks/use-toast";

const Help = () => {
  const { toast } = useToast();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    toast({
      title: "Report Submitted",
      description: "Thank you for your report. Our team will investigate.",
    });
  };

  return (
    <div className="min-h-screen bg-gradient-hero">
      <Navbar />
      
      <div className="container mx-auto px-4 pt-24 pb-20">
        <div className="max-w-6xl mx-auto space-y-8">
          {/* Header */}
          <div className="text-center animate-fade-in">
            <h1 className="text-4xl font-bold mb-4">Help & Awareness Center</h1>
            <p className="text-xl text-muted-foreground">
              Learn about education loan fraud prevention and detection
            </p>
          </div>

          {/* Infographics */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
              <CardHeader>
                <Shield className="h-12 w-12 text-primary mb-4" />
                <CardTitle>Fraud Indicators</CardTitle>
                <CardDescription>Common red flags in loan applications</CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm">
                  <li className="flex items-start gap-2">
                    <AlertCircle className="h-4 w-4 text-destructive mt-0.5 flex-shrink-0" />
                    <span>Inconsistent document metadata</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <AlertCircle className="h-4 w-4 text-destructive mt-0.5 flex-shrink-0" />
                    <span>Multiple applications with same identity</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <AlertCircle className="h-4 w-4 text-destructive mt-0.5 flex-shrink-0" />
                    <span>Tampered or edited documents</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <AlertCircle className="h-4 w-4 text-destructive mt-0.5 flex-shrink-0" />
                    <span>Mismatched biometric data</span>
                  </li>
                </ul>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.1s' }}>
              <CardHeader>
                <FileText className="h-12 w-12 text-primary mb-4" />
                <CardTitle>Case Studies</CardTitle>
                <CardDescription>Real-world fraud detection examples</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-3 text-sm">
                  <div className="p-3 bg-muted/50 rounded-lg">
                    <p className="font-semibold mb-1">Case #2024-001</p>
                    <p className="text-muted-foreground">Identity theft ring detected across 5 institutions</p>
                  </div>
                  <div className="p-3 bg-muted/50 rounded-lg">
                    <p className="font-semibold mb-1">Case #2023-456</p>
                    <p className="text-muted-foreground">Systematic document forgery operation exposed</p>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in" style={{ animationDelay: '0.2s' }}>
              <CardHeader>
                <BookOpen className="h-12 w-12 text-primary mb-4" />
                <CardTitle>Best Practices</CardTitle>
                <CardDescription>Guidelines for fraud prevention</CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm">
                  <li className="flex items-start gap-2">
                    <div className="w-1.5 h-1.5 rounded-full bg-success mt-2 flex-shrink-0" />
                    <span>Always verify original documents</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-1.5 h-1.5 rounded-full bg-success mt-2 flex-shrink-0" />
                    <span>Cross-reference with official databases</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-1.5 h-1.5 rounded-full bg-success mt-2 flex-shrink-0" />
                    <span>Conduct thorough background checks</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <div className="w-1.5 h-1.5 rounded-full bg-success mt-2 flex-shrink-0" />
                    <span>Regular staff training on fraud detection</span>
                  </li>
                </ul>
              </CardContent>
            </Card>
          </div>

          {/* FAQ Section */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
            <CardHeader>
              <div className="flex items-center gap-2">
                <HelpCircle className="h-6 w-6 text-primary" />
                <CardTitle>Frequently Asked Questions</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              <Accordion type="single" collapsible className="w-full">
                <AccordionItem value="item-1">
                  <AccordionTrigger>How accurate is the AI fraud detection?</AccordionTrigger>
                  <AccordionContent>
                    Our AI model achieves 98.2% accuracy in detecting fraudulent applications. It uses advanced machine learning algorithms trained on thousands of verified fraud cases, continuously improving with each analysis.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-2">
                  <AccordionTrigger>What documents can be analyzed?</AccordionTrigger>
                  <AccordionContent>
                    The system can analyze PAN cards, Aadhaar cards, educational certificates, income certificates, bank statements, and other relevant documents. All major document formats (PDF, JPG, PNG) are supported.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-3">
                  <AccordionTrigger>How long does the analysis take?</AccordionTrigger>
                  <AccordionContent>
                    Most analyses are completed within 2-3 minutes. Complex cases involving multiple documents or cross-verification with databases may take up to 5 minutes.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-4">
                  <AccordionTrigger>Is the data secure and confidential?</AccordionTrigger>
                  <AccordionContent>
                    Yes, we use bank-grade encryption and comply with all data protection regulations. All documents are encrypted in transit and at rest. Access is strictly controlled and logged.
                  </AccordionContent>
                </AccordionItem>
                <AccordionItem value="item-5">
                  <AccordionTrigger>What happens if fraud is detected?</AccordionTrigger>
                  <AccordionContent>
                    When fraud is detected, a detailed report is generated with evidence and risk scores. The case can be flagged for manual review, sent to investigation teams, and shared with relevant authorities as per institutional policies.
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </CardContent>
          </Card>

          {/* Report Fraud Pattern */}
          <Card className="bg-card/80 backdrop-blur-lg border-border shadow-glass animate-scale-in">
            <CardHeader>
              <div className="flex items-center gap-2">
                <MessageCircle className="h-6 w-6 text-primary" />
                <CardTitle>Report New Fraud Pattern</CardTitle>
              </div>
              <CardDescription>
                Help us improve by reporting new fraud patterns or suspicious activities
              </CardDescription>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="reporter-name">Your Name</Label>
                    <Input id="reporter-name" placeholder="Full name" required />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="reporter-email">Email</Label>
                    <Input id="reporter-email" type="email" placeholder="your.email@bank.com" required />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="pattern-title">Pattern Title</Label>
                  <Input id="pattern-title" placeholder="Brief description of the fraud pattern" required />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="pattern-details">Detailed Description</Label>
                  <Textarea 
                    id="pattern-details" 
                    placeholder="Provide detailed information about the fraud pattern, indicators, and any relevant case references..."
                    rows={6}
                    required
                  />
                </div>
                <Button type="submit" className="bg-gradient-primary">
                  Submit Report
                </Button>
              </form>
            </CardContent>
          </Card>
        </div>
      </div>

      <Footer />
    </div>
  );
};

export default Help;
