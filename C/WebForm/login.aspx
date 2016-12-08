<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="login.aspx.cs" Inherits="WebForms101.login" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body style="height: 372px">
    <form id="form1" runat="server">
    <div>
    
    </div>
        <p>
            &nbsp;</p>
        <p style="width: 72px">
            First Name:
        </p>
        <p style="width: 72px">
&nbsp;<asp:TextBox ID="txtFirst" runat="server"></asp:TextBox>
        </p>
        <p>
            Last Name:&nbsp;
        </p>
        <p style="height: 31px; width: 43px">
            <asp:TextBox ID="txtLast" runat="server"></asp:TextBox>
        </p>
        <p style="height: 31px; width: 43px">
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Button" />
        </p>
        <asp:TextBox ID="lblName" runat="server" BorderStyle="Inset"></asp:TextBox>
    </form>
</body>
</html>
