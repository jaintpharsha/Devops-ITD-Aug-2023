FROM node:10 AS source-build
WORKDIR /usr/src/app
COPY WebApp/ ./WebApp/
RUN cd WebApp && npm install @angular/cli && npm install && npm run build

FROM node:slim 
WORKDIR /root/
COPY --from=source-build /usr/src/app/WebApp/dist ./WebApp/dist
COPY package*.json ./
RUN npm install
COPY index.js .
EXPOSE 3070
ENTRYPOINT ["node"]
CMD ["index.js"]
