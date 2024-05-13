# Use a imagem oficial do Nginx
FROM nginx:latest

# Remova o arquivo de configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copie os arquivos de configuração do Nginx personalizados
COPY nginx.conf /etc/nginx/conf.d/

# Copie os arquivos do frontend para o diretório de trabalho do Nginx
COPY . /usr/share/nginx/html