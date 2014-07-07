uniform sampler2D texture0;
uniform sampler2D texture1;
uniform float time;

varying vec2 v_tex;
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye;


const float specular_power = 10.0;

void main()
{
    vec4 col = texture2D(texture0,v_tex);

   	float lambert_factor = max(dot(v_norm,v_light),0.1);

    vec3 phong = reflect(-v_eye,v_norm);
    vec3 blinn = normalize(v_eye + v_norm);

    float spec = pow(max(dot(v_light,phong),0.1), specular_power);

    //col *= lambert_factor;
    col += spec;

    col.a = 1.0;
    gl_FragColor = col;

}
