varying vec2  v_tex;
varying vec3 v_light;
varying vec3 v_eye;
uniform float time;
uniform sampler2D texture0;
uniform sampler2D texture1;

const float specular_power = 1.;

void main()
{
    vec4 textur = texture2D(texture0,v_tex);
    vec4 bump = texture2D(texture1,v_tex);
	float lambert_factor = max(dot(bump,vec4(v_light,0.)),0.);
    float phong_factor   = pow(max(dot(bump,vec4(normalize(v_light + v_eye),1.)), 0.),specular_power);

	textur *= lambert_factor;
	textur *= phong_factor;
	textur.a = 1.;

	gl_FragColor=vec4(textur);
	
}