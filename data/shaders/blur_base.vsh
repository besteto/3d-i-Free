attribute vec3 position;
attribute vec2 texcoord;
attribute vec3 normal;

uniform   mat4 modelView;
uniform   mat4 prjView;

varying vec2 v_tex;
varying vec2 v_blurTexCoords[8];
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye;

const vec3 light_position = vec3(0,0,0);
const vec3 eye_position   = vec3(0,0,0);
const float r = 1./100.;

void main()
{
	vec4 p4 = vec4(position,1);
	vec4 n4 = vec4(normal,0);

	vec3 view_pos   = vec3(p4 * modelView);
    
    v_light  = normalize(light_position - view_pos);
    v_eye    = normalize(eye_position   - view_pos);
    v_norm   = vec3(n4 * modelView);
	v_tex    = texcoord;
	
	gl_Position = p4 * modelView * prjView;
	
	v_blurTexCoords[ 0] = v_tex + vec2(-r, -r);
    v_blurTexCoords[ 1] = v_tex + vec2(-r, 0.0);
    v_blurTexCoords[ 2] = v_tex + vec2(r, 0.0);
    v_blurTexCoords[ 3] = v_tex + vec2(r, r);
    v_blurTexCoords[ 4] = v_tex + vec2(0.0, -r);
    v_blurTexCoords[ 5] = v_tex + vec2(0.0, r);
    v_blurTexCoords[ 6] = v_tex + vec2(-r, r);
    v_blurTexCoords[ 7] = v_tex + vec2(r, -r);
}

