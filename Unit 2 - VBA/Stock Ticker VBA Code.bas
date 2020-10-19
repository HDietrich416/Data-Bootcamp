Attribute VB_Name = "Module11"
Sub StockMarket1()

'The purpose of this is to summarize the unique Ticker symbols in a summary table and calculate the total Volume per Ticker.


    Dim TickerSymbol As String
    Dim TotalStockVolume As Double
    Dim SummaryRow As Integer
    Dim LastRow As Long
    Dim WS_Count As Integer
    Dim WS As Integer
    
        
      
       
            SummaryRow = 2
            TotalStockVolume = 0
    
    
            Range("i1").Value = "Ticker"
            Range("J1").Value = "Yearly Change"
            Range("K1").Value = "Percentage Change"
            Range("L1").Value = "Total Stock Volume"
    
    
            LastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
            For I = 2 To LastRow
    
                If (Cells(I + 1, 1).Value <> Cells(I, 1).Value) Then
                    TickerSymbol = Cells(I, 1).Value
                    TotalStockVolume = TotalStockVolume + Cells(I, 7).Value
            
                    Cells(SummaryRow, 9).Value = TickerSymbol
                    Cells(SummaryRow, 12).Value = TotalStockVolume
            
                    SummaryRow = SummaryRow + 1
                    TotalStockVolume = 0
            
                Else
                    TotalStockVolume = TotalStockVolume + Cells(I, 7).Value
                End If
    
            Next I
        
        

End Sub



Sub StockMarket2()

'The purpose of this is to calculate and output the yearly $change and % change for each Ticker symbol.


    Dim SummaryRow As Integer
    Dim YearlyChange As Double
    Dim PercentageChange As String
    Dim EndTickerRow As Long
    Dim BeginningTickerRow As Long
    Dim LastRow As Long
    Dim I As Long
    Dim Cell As Range
    
    SummaryRow = 2
    BeginningTickerRow = 2
    LastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    
    For I = 2 To LastRow
    
        If (Cells(I - 1, 1).Value <> Cells(I, 1).Value) Then
            BeginningTickerRow = I
        Else
            BeginningTickerRow = BeginningTickerRow
        End If
        
        If (Cells(I + 1, 1).Value <> Cells(I, 1).Value) Then
            EndTickerRow = I
            
            YearlyChange = ((Cells(EndTickerRow, 6).Value) - (Cells(BeginningTickerRow, 3).Value))
            
            If YearlyChange = 0 Then
                PercentageChange = 0
            
            ElseIf IsEmpty(Cells(BeginningTickerRow, 3).Value) = True Or Cells(BeginningTickerRow, 3).Value = 0 Then
                PercentageChange = 0
            Else
                PercentageChange = YearlyChange / (Cells(BeginningTickerRow, 3).Value)
            End If
        
     
            Cells(SummaryRow, 10).Value = YearlyChange
            Cells(SummaryRow, 11).Value = PercentageChange
        
            SummaryRow = SummaryRow + 1
    
        End If
        
    Next I
    
   


End Sub
        

Sub StockMarket3()

'The purpose of this is to format the % change and $ Change column.

    Dim Column As Integer
    Dim LastRow As Long
    
    LastRow = Cells(Rows.Count, 9).End(xlUp).Row
    
    
    For I = 2 To LastRow
        
        Cells(I, 11).NumberFormat = "0.00%"
        
        
        If Cells(I, 10).Value > 0 Then
            Cells(I, 10).Interior.Color = vbGreen
        
        ElseIf Cells(I, 10).Value < 0 Then
            Cells(I, 10).Interior.Color = vbRed
            
        End If
        
    Next I
    
    

End Sub


