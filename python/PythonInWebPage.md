# PythonInWebPage

::: {#content dir="ltr" lang="en"}
PythonInWebPage presentation systems (see [DataRepresentation](DataRepresentation)) encourages the use of Python source code embedded in the content of a Web page (or other resource to be presented) such that the execution of the code causes the surrounding content to be transformed in some way. A classic, simplified example of this concept using JSP syntax might look like this:

    <table>
      <%
      for item in items:
        %>
        <tr>
          <th>Name</th>
          <td><%= item.name %></td>
        </tr>
        <%
      %>
    </table>

or like this ([PythMl](http://adullact.net/projects/pythml/){.http} syntax)

    <table>
    for item in items:
      <tr>
      <th>Name</th>
      <td>`item.name`</td>
      </tr>
    </table>

Note that Python\'s need for indentation raises issues with how code blocks are to be delimited, especially in content which may itself be indented according to a different scheme, hence the use of an empty code block after the body of the loop in the above example.

Comparable technologies include: ASP (Active Server Pages), JSP ([JavaServer](./JavaServer.html){.nonexistent} Pages), PHP.
:::
